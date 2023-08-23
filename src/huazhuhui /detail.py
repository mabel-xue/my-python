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

headers = {
    'Cookie': '_hudVID=7f4a8834-3a59-2b1f-18a2-3de44b2f818c; _ga=GA1.2.1882665499.1690974883; gr_user_id=7c5b5775-4d31-466b-80b9-e036ff7e719b; ec=LT4tUfS4-1690974884269-b2d367a88e0871833201250; c=LT4tUfS4-1690974884269-b2d367a88e0871833201250; _exid=Bp7viK6oGNi2FdtCZ6i125cCUsi6kzsg0dQ8VWIwztuOzzBwAMKRzgj7pNrnQXC%2F3fu18gEW7NY3QhGHKUpGQA%3D%3D; _xid=wtLHL8m1c1Mfg95jphs8YDG1yXb7iASAuSRReYBm4Jk%3D; _efmdata=fFfZK2aAZedzVnPmugUrqT%2Btq0KrZJ2Y1uI7tYMnzN30MSC7qaqUeh6Dy8q2%2BTJls5PZ93BvQOfmCa9lZ6Hhr5wwAYteAE6gARCrvxojaL0%3D; _fmdata=yXy0DbbAfWcFvaOvBSdB5lbciyA5oGZw94EDh0RtmMOO5jQxfH0wUT08ex%2BuikmFGHSkJXnS9QBXVfUYrsfGCw%3D%3D; _hudSource=; _HZ_I_SessionId=a91ee4ba-d150-4cf1-b100-f43828def873; userToken=36dac08c96c746b3b5c8a77eb2d79877262571721; _hudSID=1692805042067_6; hud_refer=hrewards.huazhu.com/hotel/detail|10007,hrewards.huazhu.com/hotel|10006; _hudPVID=24; _hudSID_TS=1692807322575'
}

hotelList = get_data(request_url, {
    'checkInDate': '2023-08-29',
    'checkOutDate': '2023-08-31',
    'hotelId': '8100061',
}, headers)

data = [{
    'typeRoomName': item['typeRoomName'],
    'roomArea': item['roomArea'],
    'amount': item['ratePlanCodeList'][0]['dailyPrice'][0]['prices'][0]['amount'],
    'marketPrice': item['ratePlanCodeList'][0]['dailyPrice'][0]['prices'][0]['marketPrice'],
    # 'price': item['ratePlanCodeList'][0]['dailyPrice'][0]['prices'][0]['amount']*0.85,
    'hasWindow': item['hasWindow'],
    'bedSize': item['bedSize']
} for item in hotelList['content']['roomPriceList']['roomList']]


print(json.dumps(data, ensure_ascii=False, indent=4))
