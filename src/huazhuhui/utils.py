# -*- coding: utf-8 -*-

import requests
from datetime import datetime, timedelta


def handle_res(response):
    response.raise_for_status()  # 检查响应状态码
    return response.json()


def get_data(url, params=None, headers=None):
    try:
        response = requests.get(url, params=params, headers=headers)
        return handle_res(response)
    except requests.exceptions.RequestException as e:
        # 处理请求异常
        print(e)

def calculate_date_range(month, date):
    # 将 month 和 date 转换为日期对象
    s = month[:2]+date[:2]
    e = month[-2:]+date[-2:]
    start_date = datetime.strptime(s, '%m%d')
    end_date = datetime.strptime(e, '%m%d')

    # 计算中间的日期范围
    date_range = []
    current_date = start_date

    while current_date < end_date:
        date_range.append(current_date.strftime('%m%d'))
        current_date += timedelta(days=1)

    return date_range
