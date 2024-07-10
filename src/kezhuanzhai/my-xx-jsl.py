from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urlparse, parse_qs
import re
import datetime
from datetime import timedelta
import pandas as pd
from tabulate import tabulate

def output_excel(df):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f'my_xx_{timestamp}.xlsx'
    df.to_excel(output_file, index=False)


def get_future_workday(days):
    today = datetime.datetime.now()
    weekdays = 0
    while weekdays < days:
        today += timedelta(days=1)
        if today.weekday() < 5:  # 0-4 表示周一到周五
            weekdays += 1
    return today.strftime("%y-%m-%d")


# url = "https://www.ninwin.cn/index.php?m=cb&show_cb_only=Y&show_listed_only=Y" # 宁稳
url = "http://localhost:3000/data/cbnew/adjust_list" # 集思录
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
    columns=["转债名", "price", "下修信息", "下修时间点", "下修是否不可低于净资产", "pb"]
)

response = requests.get(url, headers=headers)
result = response.json()['rows']
filtered_rows = list(filter(lambda row: row["id"] in codes, result))

for d in filtered_rows:
    item=d["cell"]
    name=item['bond_nm']
    adjust_remain_days=item['adjust_remain_days']
    adj_tips=item['adj_tips']
    pb=item['pb']
    price=item['price']
    is_asset_limit="Y" if adj_tips.startswith("S") else "N" if adj_tips=="R" else "-"
    xiaxiu=''
    future_workday=''
    if ((adjust_remain_days>-2) & (adj_tips=="S S")):
       xiaxiu='刚下修'
    elif(adjust_remain_days==0):
      xiaxiu='审议中'
    elif(adj_tips==''):
       xiaxiu='-'
    else:
      xiaxiu=f'已满足{15-adjust_remain_days}天'
      future_workday = get_future_workday(adjust_remain_days)
       
    df.loc[len(df)] = [name, price, xiaxiu, future_workday, is_asset_limit, pb]

# print(json.dumps(result, indent=4, ensure_ascii=False))
print(tabulate(df.sort_values(by="下修信息")))
output_excel(df)