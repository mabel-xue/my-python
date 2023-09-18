# -*- coding: utf-8 -*-

import requests
import re
import json
import codecs
import os
import datetime
from bs4 import BeautifulSoup
import math
# from src.api import get_data


def gen_json(data):
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    # print(json_str)

    with codecs.open('data1.json', 'w', encoding="utf-8") as f:
        f.write(json_str)


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


request_url = 'https://hweb-hotel.huazhu.com/hotels/hotel/list'

HotelStyle = {
    # 汉庭
    'ht': 4,
    # 全季
    'qj': 2,
    # 桔子
    'jz': 16,
    # 桔子水晶
    'jzsj': 14,
    # 汉庭优佳
    'htyj': 18,
    # 海友
    'hy': 5,
}

param = {
    'checkInDate': '2023-09-23',
    'checkOutDate': '2023-09-24',
    'cityName': '南阳',
    # 'hotelStyle': '2',
    # 'hotelStyle': '2,4,14,16,18',
    # 'sortBy':0
    'pageSize': 20,
    'pageIndex': 1
}

hotelList = get_data(request_url, param)

allH = []

totalPage = int(math.ceil((float(hotelList['content']['totalCount'])+1)/20.0))

print(hotelList['content']['totalCount'], totalPage)

for item in range(1, totalPage+1):
    print(item)
    param['pageIndex'] = item
    list = get_data(request_url, param)

    data = [{
        'hotelId': item['hotelId'],
        'hotelName': item['hotelName'],
        'hotelAddressShort': item['hotelAddressShort'],
        # 'lowestMaretPrice': item['lowestMaretPrice'],
        # 'price': item['lowestMaretPrice']*0.85
    } for item in list['content']['hotelList']]
    # print(json.dumps(data, ensure_ascii=False, indent=2))
    allH.extend(data)

gen_json(allH)
