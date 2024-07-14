from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urlparse, parse_qs
import re
import datetime
from datetime import timedelta
import pandas as pd
from tabulate import tabulate
import akshare as ak

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def output_excel(df):
    output_file = f"下修审议中_{timestamp}.xlsx"
    df.to_excel(output_file, index=False)


def get_future_workday(days):
    today = datetime.datetime.now()
    weekdays = 0
    while weekdays < days:
        today += timedelta(days=1)
        if today.weekday() < 5:  # 0-4 表示周一到周五
            weekdays += 1
    return today.strftime("%Y-%m-%d")


def get_response(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    return requests.get(url, headers=headers).json()


def post_response(url, data):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    return requests.post(url, data, headers=headers).json()


bond_zh_cov_df = ak.bond_cb_jsl(
    cookie="kbz__Session=ipkbct7kln5q9jjutjm8806c31; Hm_lvt_164fe01b1433a19b507595a43bf58262=1720267354; HMACCOUNT=22FE3916F7FABF53; kbz_newcookie=1; kbzw__Session=20otvclbi7vdcll53u6421ptc5; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1720879663; kbz__user_login=1ubd08_P1ebax9aX5MPYxt_w1tWCr6blyuzf7tHoxdHVjKSU2trZnbLSsMSulKbekaWUrK2onqvS3ZisxqzexdaSlbSi3uLQ1b-hkqSvlKSVqZqwlrrA1b-hkqqqkaiYra-rn5qnpLe3v9Cjrt_b3eXhyqihpZKWicDZxNnP6Ojo0bSMwNDqxt-YrtHElMjIidGMqJLVkqjXmJmBtenl1d7D3MTByuenlqOYoqyriaG3v7bDrZ-YzdnM2Zm8ztzX5ouWpNvq0N3Go6qnn6ecpZKkkZPLwtbC5uKknqyjpZWs; SERVERID=5452564f5a1004697d0be99a0a2e3803|1720879666|1720879049"
)
if len(bond_zh_cov_df) < 40:
    raise Exception("请更新集思录cookie！")


df = pd.DataFrame(
    columns=[
        "代码",
        "转债名",
        "转债价格",
        "下修信息",
        "预估下修日",
        "下修是否不可低于净资产",
        "下修剩余天",
        # "pb",
    ]
)

url = "https://app.jisilu.cn/data/cbnew/adjust_list/"  # 集思录-下修
result = get_response(url)["rows"]

for d in result:
    item = d["cell"]
    id = item["bond_id"]
    name = item["bond_nm"]
    adjust_remain_days = item["adjust_remain_days"]
    adj_tips = item["adj_tips"]
    # pb = item["pb"]
    price = item["price"]
    is_asset_limit = (
        "Y" if adj_tips.startswith("S") else "N" if adj_tips == "R" else "-"
    )
    xiaxiu = ""
    future_workday = ""
    if (adjust_remain_days == -1) & (adj_tips == "S S"):
        xiaxiu = "刚下修"
    elif adjust_remain_days == -1:
        xiaxiu = "未满足"
    elif adjust_remain_days == 0:
        xiaxiu = "已满足"
        # url = "https://app.jisilu.cn/data/cbnew/announcement_list/"  # 集思录-公告
        # result = post_response(url, {
        #   'code': id
        #   })["rows"]

    else:
        xiaxiu = f"已满足{15-adjust_remain_days}天"
        future_workday = get_future_workday(adjust_remain_days)

    df.loc[len(df)] = [
        id,
        name,
        price,
        xiaxiu,
        future_workday,
        is_asset_limit,
        adjust_remain_days,
        # pb,
    ]

df = df[df["下修信息"] == "已满足"]

print("已满足：", len(df))
df = pd.merge(df, bond_zh_cov_df, on="代码", how="inner").drop_duplicates()

print("已满足_合并后：", len(df))
# 进一步过滤
df = df[
    (~df["转债名"].endswith("退债"))
    # & (df["转债价格"].astype(float) < 115.0)
    # & ((df["下修剩余天"].astype(int)) < 11)
    # & (
    #     ((df["下修是否不可低于净资产"] == "Y") & (df["正股PB"].astype(float) > 1.0))
    #     | (df["下修是否不可低于净资产"] != "Y")
    # )
]
print("已满足_过滤后：", len(df))

selected_columns = [
    "代码",
    "转债名",
    "转债价格",
    # "下修信息",
    "预估下修日",
    # "下修是否不可低于净资产",
    "正股代码",
    "正股名称",
    # "正股PB",
    "到期时间",
    # "剩余年限",
    # "剩余规模",
]

df = df.loc[:, selected_columns]

print(tabulate(df.sort_values(by="到期时间")))
output_excel(df.sort_values(by="到期时间"))
