# -*- coding: utf-8 -*-

import json
import constant
import math
import requests

def handle_res(response):
    response.raise_for_status()  # 检查响应状态码
    return response.json()

request_url = 'https://hweb-hotel.huazhu.com/hotels/hotel/detail'
month = '0909'
date = '1819'
params = {
    'checkInDate': '2023-'+month[:2]+'-'+date[:2],
    'checkOutDate': '2023-'+month[-2:]+'-'+date[-2:],
    'hotelId': '9002101',
}
requests.get(request_url, params=params)
print(request_url)