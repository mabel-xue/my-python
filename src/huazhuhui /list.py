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
headers = {
    'Cookie': '_hudVID=51280303-8e08-01ae-3d12-667a260427f4; _hudSource=; _hudSID=1692839072641_4; _HZ_I_SessionId=5581db4d-da60-4f9f-bbed-2d3ba9f2fafd; userToken=487644794fd0448d87b440f0861b3671262571721; hud_refer=hrewards.huazhu.com/|10001,hpassport.huazhu.com/|10018,hrewards.huazhu.com/hotel|10013; _hudPVID=31; _hudSID_TS=1692839094344'
}

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
month = '0909'
date = '1617'
hotelList = get_data(request_url, {
    'checkInDate': '2023-'+month[:2]+'-'+date[:2],
    'checkOutDate': '2023-'+month[:2]+'-'+date[:2],
    'cityName': '张家口',
    'hotelStyle': HotelStyle['qj'],
    # 'sortBy':0
    'pageSize': 20,
    'pageIndex': 1,
    # 'keyword': '全季天津中北新城市中心酒店',
}, headers)

data = [{
    'hotelId': item['hotelId'],
    'hotelName': item['hotelName'],
    'hotelAddressShort': item['hotelAddressShort'],
    # 'lowestMaretPrice': item['lowestMaretPrice'],
    # 'hotelLowestPrice': item['hotelLowestPrice']
} for item in hotelList['content']['hotelList']]


print(json.dumps(data, ensure_ascii=False, indent=2).encode('utf-8'))
