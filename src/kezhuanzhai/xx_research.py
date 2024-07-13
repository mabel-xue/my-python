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


def output_excel(df):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"my_xx_{timestamp}.xlsx"
    df.to_excel(output_file, index=False)


def get_future_workday(days):
    today = datetime.datetime.now()
    weekdays = 0
    while weekdays < days:
        today += timedelta(days=1)
        if today.weekday() < 5:  # 0-4 表示周一到周五
            weekdays += 1
    return today.strftime("%y-%m-%d")


bond_zh_cov_df = ak.bond_cb_jsl(
    cookie="kbz_newcookie=1; kbzw__Session=3kb0dab06es946vbbj6aemevd5; Hm_lvt_164fe01b1433a19b507595a43bf58262=1719233983,1719324706; HMACCOUNT=26BD2E5A129E88F1; kbzw__user_login=7Obd08_P1ebax9aX5MPYxuPv6N2Cq47k2ujc8NvpxtS-oqum3sLUla3frsuxn6rIppaqr6erlqLH2q-rzrLS28ingrKk6OHFzr6fqqagrKCrl5ecpLjH1r6bkqurpZ-rnaiTq4KypMi5v82Mwejv0uXY2JGrj6eXm8XC08ri7eTc4aeXq-TV3OOTxcLTgcPMlcGZnafBp5bWrpyYouDR4N7Mztu34NallqquoauXkIm_wcm2xZiXzt_M3Je63cTb0J2ZuNHr2-THpZKpraGoj6CPpJnIyt_N6cullqquoauX; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1720795179"
)
if len(bond_zh_cov_df) < 40:
    raise Exception("请更新集思录cookie！")

url = "https://www.jisilu.cn/webapi/cb/delisted/"  # 集思录
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

df = pd.DataFrame(
    columns=[
        "代码",
        "转债名",
        "转债价格",
        "下修信息",
        "下修满足时间点",
        "下修是否不可低于净资产",
        "下修剩余天",
        # "pb",
    ]
)

response = requests.get(url, headers=headers)
result = response.json()["data"]

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
        xiaxiu = "审议中"
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
    ]

df = df[df["下修满足时间点"] != ""]
print(len(df))
df = pd.merge(df, bond_zh_cov_df, on="代码", how="inner").drop_duplicates()

print(len(df))
# 进一步过滤
df = df[
    (df["到期时间"] > df["下修满足时间点"])
    & (df["转债价格"] < 130)
    & (df["下修剩余天"] < 11)
]
print(len(df))
# print(tabulate(df.sort_values(by="到期时间")))
# output_excel(df.sort_values(by="到期时间"))

selected_columns = [
    "代码",
    "转债名",
    "转债价格",
    "下修信息",
    "下修满足时间点",
    "下修是否不可低于净资产",
    "正股代码",
    "正股名称",
    "正股PB",
    "到期时间",
    "剩余年限",
    "剩余规模",
]

df = df.loc[:, selected_columns]

# print(json.dumps(result, indent=4, ensure_ascii=False))
print(tabulate(df.sort_values(by="到期时间")))
output_excel(df.sort_values(by="到期时间"))
