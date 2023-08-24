# -*- coding: utf-8 -*-

import requests
import re
import json
import codecs
import os
import datetime
from bs4 import BeautifulSoup


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

headers = {
    'Cookie': '_hudVID=51280303-8e08-01ae-3d12-667a260427f4; _hudSource=; _hudSID=1692839072641_4; _HZ_I_SessionId=5581db4d-da60-4f9f-bbed-2d3ba9f2fafd; userToken=487644794fd0448d87b440f0861b3671262571721; hud_refer=hrewards.huazhu.com/|10001,hpassport.huazhu.com/|10018,hrewards.huazhu.com/hotel|10013; _hudPVID=31; _hudSID_TS=1692839094344'
}

params = {
    'checkInDate': '2023-08-25',
    'checkOutDate': '2023-08-27',
    'hotelId': '1100003',
}

hotelList = get_data(request_url, params=params, headers=headers)

data = [{
    'typeRoomName': item['typeRoomName'],
    'roomArea': item['roomArea'],
    'amount': item['ratePlanCodeList'][0]['dailyPrice'][0]['prices'][0]['amount'],
    'marketPrice': item['ratePlanCodeList'][0]['dailyPrice'][0]['prices'][0]['marketPrice'],
    # 'price': item['ratePlanCodeList'][0]['dailyPrice'][0]['prices'][0]['amount']*0.85,
    'hasWindow': item['hasWindow'],
    'bedSize': item['bedSize']
} for item in hotelList['content']['roomPriceList']['roomList']]

# print(json.dumps(data, ensure_ascii=False, indent=4))
print(data.encode('utf-8').decode('unicode-escape'))
