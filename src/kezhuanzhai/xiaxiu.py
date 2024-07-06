from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urlparse, parse_qs
import re
import datetime
from datetime import timedelta


def get_future_workday(days):
    today = datetime.datetime.now()
    weekdays = 0
    while weekdays < days:
        today += timedelta(days=1)
        if today.weekday() < 5:  # 0-4 表示周一到周五
            weekdays += 1
    return today.strftime('%Y-%m-%d')


url = 'https://www.ninwin.cn/index.php?m=cb&show_cb_only=Y&show_listed_only=Y'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

codes = ['113542',
         '110063',
         '127041',
         '127019',
         '128124',
         '110072',
         '123128',
         '118008',
         '118031',
         '110062',
         '128044',
         '127022']
response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    elements = soup.select('.cb_name_id a')
    result = []

    for element in elements:
        href = element.get('href')
        content = element.get_text()

        # 获取下修时间
        res = requests.get(href, headers=headers)
        if res.status_code == 200:
            soup2 = BeautifulSoup(res.content, 'html.parser')
            pattern = r'下修条件：.*?【<span style="color: inherit">已满足(\d+)天</span>】'
            match = re.search(pattern, soup2.get_text())
            if match:
                days_satisfied = int(match.group(1))
                days_remaining = 15 - days_satisfied
                future_workday = get_future_workday(days_remaining)
                print(future_workday)
            else:
                print("未找到下修条件已满足的天数")

        result.append({'href': href, 'content': content, })

    print(json.dumps(result, indent=4, ensure_ascii=False))
