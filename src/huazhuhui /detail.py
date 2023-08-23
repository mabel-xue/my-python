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


request_url = 'https://hweb-hotel.huazhu.com/hotels/hotel/detail'

hotelList = get_data(request_url, {
    'checkInDate': '2023-08-25',
    'checkOutDate': '2023-08-26',
    'hotelId': '8000151',
})

data = [{
    'typeRoomName': item['typeRoomName'],
    'roomArea': item['roomArea'],
    'marketPrice': item['marketPrice'],
    'price': item['marketPrice']*0.85,
    'hasWindow': item['hasWindow'],
    'bedSize': item['bedSize']
} for item in hotelList['content']['roomPriceList']['roomList']]


print(json.dumps(data, ensure_ascii=False, indent=4))
