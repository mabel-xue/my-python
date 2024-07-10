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

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


def output_excel(df):
    output_file = f"可转债下修审议中_{timestamp}.xlsx"
    df.to_excel(output_file, index=False)


def get_future_workday(days):
    today = datetime.datetime.now()
    weekdays = 0
    while weekdays < days:
        today += timedelta(days=1)
        if today.weekday() < 5:  # 0-4 表示周一到周五
            weekdays += 1
    return today.strftime("%y-%m-%d")


cookie = "kbz__Session=ipkbct7kln5q9jjutjm8806c31; Hm_lvt_164fe01b1433a19b507595a43bf58262=1720267354; HMACCOUNT=22FE3916F7FABF53; kbz_newcookie=1; kbz__user_login=1ubd08_P1ebax9aX5MPYxt_w1tWCr6blyuzf7tHoxdHVjKSU2trZnbLSsMSulKbekaWUrK2onqvS3ZisxqzexdaSlbSi3uLQ1b-hkqSvlKSVqZqwlrrA1b-hkqqqkaKXq6ysnpqnpLe3v9Cjrt_b3eXhyqihpZKWicDZxNnP6Ojo0bSMwNDqxt-YrtHElMjIidGMqJLVkqjXmJmBtenl1d7D3MTByuenlqOYoqyriaG3v7bDrZ-YzdnM2Zm8ztzX5ouWpNvq0N3Go6qnn6ecpZKkkZPLwtbC5uKknqyjpZWs; kbzw__Session=20otvclbi7vdcll53u6421ptc5; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1720271397; kbzw__user_login=7Obd08_P1ebax9aX5MPYxuPv6N2Cq47k2ujc8NvpxtS-oqum3sLUla3frsuxn6rIppaqr6erlqLH2q-rzrLS28ingrKk6OHFzr6fqqagrKCrl5ecpLjH1r6bkqurpZuwnaqbrYKypMi5v82Mwejv0uXY2JGrj6eXm8XC08ri7eTc4aeXq-TV3OOTxcLTgcPMlcGZnafBp5bWrpyYouDR4N7Mztu34NallqquoauXkIm_wcm2xZiXzt_M3Je63cTb0J2ZuNHr2-THpZKpraGoj6CPpJnIyt_N6cullqquoauX; SERVERID=0e73f01634e37a9af0b56dfcd9143ef3|1720271401|1720270672"

url = "https://app.jisilu.cn/data/cbnew/adjust_list/"


bond_zh_cov_df = ak.bond_cb_jsl(cookie=cookie)
if len(bond_zh_cov_df) < 40:
    raise Exception("请更新集思录cookie！")

# 过滤下修机会的可转债
bond_zh_cov_df = bond_zh_cov_df[bond_zh_cov_df["转股价"] > bond_zh_cov_df["正股价"]]

df = pd.DataFrame(
    columns=[
        "转债代码",
        "转债名称",
        # "下修信息",
        "下修公告预计时间",
        "下修是否不可低于净资产",
        "到期时间",
    ]
)

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    result = []

    codes = bond_zh_cov_df["代码"].tolist()
    matching_elements = soup.find_all("tr", {"data-cbcode": lambda x: x in codes})
    print(len(matching_elements))

    for index, element in enumerate(matching_elements):
        # 分批保存数据
        if index % 100 == 0:
            df.to_csv("find_xx_ing_{timestamp}.csv")
            print(tabulate(df.sort_values(by="下修公告预计时间")))

        # 拿到详情 link
        link_element = element.select_one(".cb_name_id a")
        print(index)

        if link_element:
            href = link_element.get("href")
            name = re.sub(r"[^0-9\u4e00-\u9fff]", "", link_element.get_text())
            future_workday = ""
            # 请求转债详情
            res = requests.get("https://www.ninwin.cn/" + href, headers=headers)
            if res.status_code == 200:
                soup2 = BeautifulSoup(res.content, "html.parser")
                # 下修情况
                target_span = soup2.find(
                    "span", title=lambda x: x and "下修" in x, class_=False
                )
                xiaxiu = ""
                future_workday = ""
                if target_span:
                    xiaxiu = target_span.find("span").text
                    # 获取下修时间点
                    if xiaxiu == "审议中":
                        body_table = soup2.find("table", {"class": "body"})
                        if body_table:
                            first_row = body_table.find_all("tr")[1]
                            second_cell = first_row.find_all("td")[1]
                            future_workday = second_cell.text
                            if len(future_workday) == 8:
                                future_workday = "20" + future_workday
                    # elif xiaxiu.startswith("已满足"):
                    #     pattern = r"已满足(\d+)天"
                    #     match = re.search(pattern, xiaxiu)
                    #     if match:
                    #         days_satisfied = int(match.group(1))
                    #         days_remaining = 15 - days_satisfied
                    #         future_workday = get_future_workday(days_remaining)
                    else:
                        continue
                else:
                    continue

                is_asset_limit = ""
                pattern = r"下修后不可低于审计的每股净资产"
                match = re.search(pattern, soup2.get_text())
                if match:
                    is_asset_limit = "是"

                target_info = bond_zh_cov_df[
                    bond_zh_cov_df["转债名称"].astype(str) == name
                ].iloc[0]
                print(index, name, future_workday)

                df.loc[len(df)] = [
                    target_info["代码"],
                    name,
                    future_workday,
                    is_asset_limit,
                    target_info["到期时间"],
                ]

        time.sleep(2)

    # print(json.dumps(result, indent=4, ensure_ascii=False))
    # print(tabulate(df.sort_values(by="下修信息")))
    df.to_csv("find_xx_ing.csv")
    print(tabulate(df.sort_values(by="下修公告预计时间")))
    output_excel(df.sort_values(by="下修公告预计时间"))

# 打开默认浏览器的新标签页
webbrowser.open_new_tab("https://www.example.com")
