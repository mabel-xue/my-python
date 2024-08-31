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
import webbrowser
import time
import os

# 获取当前脚本文件所在目录的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 构建 nw.html 文件的绝对路径
file_path = os.path.join(script_dir, "../nw.html")
xxfile_path = os.path.join(script_dir, "../nw_xx.html")


def output_excel(df, name):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{name}_{timestamp}.xlsx"
    df.to_excel(output_file, index=False)


def get_future_workday(days):
    today = datetime.datetime.now()
    weekdays = 0
    while weekdays < days:
        today += timedelta(days=1)
        if today.weekday() < 5:  # 0-4 表示周一到周五
            weekdays += 1
    return today.strftime("%y-%m-%d")


df = pd.DataFrame(
    columns=[
        "转债代码",
        "转债名称",
        "转债价格",
        # "下修信息",
        # "下修信息详情",
        "提交审议时间",
        "正股代码",
        "正股名称",
        "到期日",
    ]
)

with open(file_path, "r") as file:
    html_content = file.read()
with open(xxfile_path, "r") as file2:
    xx_html_content = file2.read()

soup = BeautifulSoup(html_content, "html.parser")
xxsoup = BeautifulSoup(xx_html_content, "html.parser")
xx_elements = xxsoup.find(id="cb_hq").find_all("tr", attrs={"data-id": True})
result = []

tr_elements = soup.find("tbody").find_all("tr")
print(len(tr_elements))


for tr in xx_elements:
    code = tr.find("td", class_="bond_code_id").text.strip()
    state_text = tr.find_all("td", class_=re.compile(r"\bcount\b\s*"))[2]
    extra = state_text.find("span").text
    xx_state = state_text.text.strip(extra)
    if xx_state in ["审议中"]:
        xx_info_des = state_text.get("title")
        stock_code = tr.get("data-stock_code")
        xx_date = "-"
        # if xx_state == "审议中":
        pattern = r"(\d{4}-\d{2}-\d{2})提交股东大会审议"
        match = re.search(pattern, xx_info_des)
        if match:
            xx_date = match.group(1)
        cb_code = tr.get("data-cb_code")
        try:
            bond_cb_profile_sina_df = ak.bond_cb_profile_sina(symbol=cb_code)
            remind_days = bond_cb_profile_sina_df.iloc[8, 1]
        except Exception as e:
            print(f"Unexpected error: {e}")
            remind_days = "-"
        stock_individual_info_em_df = ak.stock_individual_info_em(symbol=stock_code[2:])
        data = {
            "data-cbcode": code,
            "data-cb_name": tr.get("data-cb_name"),
            "data-cb_price": tr.find("td", class_="cb_price2_id").text.strip(),
            # "xx-info": xx_state,
            # "xx-info-des": xx_info_des,
            "xx-date": xx_date,
            "stock_code": stock_code[2:],
            "data-stock_name": stock_individual_info_em_df.iloc[5, 1],
            "remind_days": remind_days,
        }
        df.loc[len(df)] = list(data.values())

# print(json.dumps(result, indent=4, ensure_ascii=False))
# print(tabulate(df.sort_values(by="下修信息")))
# df.to_csv("find_xx_ing.csv")
df = df.sort_values(by="提交审议时间")
print(tabulate(df))
output_excel(df, "下修审议中")
