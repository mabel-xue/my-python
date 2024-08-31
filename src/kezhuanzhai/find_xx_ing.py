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
    cookie="kbzw__Session=3kb0dab06es946vbbj6aemevd5; HMACCOUNT=26BD2E5A129E88F1; kbz_newcookie=1; Hm_lvt_164fe01b1433a19b507595a43bf58262=1721920140; kbzw__user_login=7Obd08_P1ebax9aX5MPYxuPv6N2Cq47k2ujc8NvpxtS-oqum3sLUla3frsuxn6rIppaqr6erlqLH2q-rzrLS28ingrKk6OHFzr6fqqagrKCrl5ecpLjH1r6bkqurp5mwoquZrYKypMi5v82Mwejv0uXY2JGrj6eXm8XC08ri7eTc4aeXq-TV3OOTxcLTgcPMlcGZnafBp5bWrpyYouDR4N7Mztu34NallqquoauXkIm_wcm2xZiXzt_M3Je63cTb0J2ZuNHr2-THpZKpraGoj6CPpJnIyt_N6cullqquoauX; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1722164181"
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
        # result = get_response(url

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
