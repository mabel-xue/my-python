import math
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
    output_file = f"已下修_research_{timestamp}.xlsx"
    df.to_excel(output_file, index=False)


def get_future_workday(days):
    today = datetime.datetime.now()
    weekdays = 0
    while weekdays < days:
        today += timedelta(days=1)
        if today.weekday() < 5:  # 0-4 表示周一到周五
            weekdays += 1
    return today.strftime("%y-%m-%d")


# 计算两个日期之间的间隔天数
def get_days(date1_str, date2_str):
    date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
    days_diff = (date1 - date2).days
    return days_diff


def convert_to_ymd(days):
    d = days
    years = math.floor(d / 365)
    remaining_days = d % 365
    months = math.floor(remaining_days / 30)
    days_remaining = remaining_days % 30

    return str(years) + "年" + str(months) + "月" + str(days_remaining) + "日"


df = pd.DataFrame()

# bond_zh_cov_df = ak.bond_zh_cov()

url = "https://app.jisilu.cn/data/cbnew/delisted/"  # 集思录
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)
result = response.json()["rows"]
print("total results:", len(result))

# try:
for i, d in enumerate(result):
    item = d["cell"]
    bond_id = item["bond_id"]
    first_dt = item["first_dt"]
    item_df = ak.bond_cb_adj_logs_jsl(symbol=bond_id)
    if len(item_df) > 0:
        print(i, item_df)
        # 添加属性
        item_df["上市时间"] = first_dt
        item_df["间隔时长"] = item_df.apply(
            lambda row: (
                row["股东大会日"]
                - datetime.datetime.strptime(first_dt, "%Y-%m-%d").date()
            ).days,
            axis=1,
        )
        # item_df["间隔时长_年月日"] = item_df[ite÷m_df[convert_to_ymd(item_df["间隔时长"])

        if i == 0:
            df = item_df.head(0).copy()
        last_row = item_df.iloc[-1]

        df = pd.concat([df, last_row.to_frame().T], ignore_index=True)

# except Exception as e:
#     print("Error: ", e)

# selected_columns = [
#     "代码",
#     "转债名",
#     "转债价格",
#     "下修信息",
#     "下修满足时间点",
#     "下修是否不可低于净资产",
#     "正股代码",
#     "正股名称",
#     "正股PB",
#     "到期时间",
#     "剩余年限",
#     "剩余规模",
# ]

# df = df.loc[:, selected_columns]

df = df.sort_values(by="间隔时长")
print(tabulate(df))
output_excel(df)
