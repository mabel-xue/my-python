from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urlparse, parse_qs
import re
import datetime
from datetime import timedelta
import pandas as pd
from tabulate import tabulate


def get_future_workday(days):
    today = datetime.datetime.now()
    weekdays = 0
    while weekdays < days:
        today += timedelta(days=1)
        if today.weekday() < 5:  # 0-4 表示周一到周五
            weekdays += 1
    return today.strftime("%y-%m-%d")


url = "https://www.ninwin.cn/index.php?m=cb&show_cb_only=Y&show_listed_only=Y"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

codes = [
    "113542",
    "110063",
    "127041",
    "127019",
    "128124",
    "110072",
    "123128",
    "118008",
    "118031",
    "110062",
    "128044",
    "127022",
]

df = pd.DataFrame(
    columns=["转债名", "下修信息", "下修时间点", "下修是否不可低于净资产", "强赎信息"]
)

response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    result = []

    matching_elements = soup.find_all("tr", {"data-cbcode": lambda x: x in codes})

    for element in matching_elements:
        # 拿到详情 link
        link_element = element.select_one(".cb_name_id a")

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
                    if xiaxiu == "不下修":
                        pattern = r"(\d{4}-\d{2}-\d{2})前暂不行使下修"
                        match = re.search(pattern, target_span.get("title"))
                        if match:
                            future_workday = match.group(1)
                    if xiaxiu == "审议中":
                        body_table = soup2.find("table", {"class": "body"})
                        if body_table:
                            first_row = body_table.find_all("tr")[1]
                            second_cell = first_row.find_all("td")[1]
                            future_workday = second_cell.text
                    if xiaxiu.startswith("已满足"):
                        pattern = r"已满足(\d+)天"
                        match = re.search(pattern, xiaxiu)
                        if match:
                            days_satisfied = int(match.group(1))
                            days_remaining = 15 - days_satisfied
                            future_workday = get_future_workday(days_remaining)
                else:
                    xiaxiu = ""

                is_asset_limit = 0
                pattern = r"下修后不可低于审计的每股净资产"
                match = re.search(pattern, soup2.get_text())
                if match:
                    is_asset_limit = 1

                # 强赎
                target_span_qs = soup2.find(
                    "span", title=lambda x: x and "强赎" in x, class_=False
                )
                qs = ""
                qs_workday = ""
                if target_span_qs:
                    qs = target_span_qs.find("span").text

                print(name, xiaxiu, future_workday, is_asset_limit)
                df.loc[len(df)] = [name, xiaxiu, future_workday, is_asset_limit, qs]

    # print(json.dumps(result, indent=4, ensure_ascii=False))
    print(tabulate(df.sort_values(by="下修信息")))
