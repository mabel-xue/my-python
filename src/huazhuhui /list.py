# -*- coding: utf-8 -*-

import requests
import re
import json
import codecs
import os
import datetime
from bs4 import BeautifulSoup
# from src.api import get_data


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
    # 公共事业
    'jz': 16,
    # 航空机场
    'jzsj': 14,
    # 房地产开发
    'htyj': 18,
    'hy': 5,
}

hotelList = get_data(request_url, {
    'checkInDate': '2023-08-26',
    'checkOutDate': '2023-08-27',
    'cityName': '如皋',
    'hotelStyle': HotelStyle['qj'],
    # 'sortBy':0
    'pageSize': 20,
    'pageIndex': 1
})

data = [{
    'hotelId': item['hotelId'],
    'hotelName': item['hotelName'],
    'hotelAddressShort': item['hotelAddressShort'],
    'lowestMaretPrice': item['lowestMaretPrice'],
    'price': item['lowestMaretPrice']*0.85
} for item in hotelList['content']['hotelList']]


print(json.dumps(data, ensure_ascii=False, indent=2))
