# -*- coding: utf-8 -*-

import json
from utils import get_data
import constant
import math

request_url = 'https://hweb-hotel.huazhu.com/hotels/hotel/detail'

alreadyBook = [
    "杭州",
    "西安",
    "淄博",
    "北京",
    "上海",
    "连云港",
    "济南",
    "洛阳",
    "烟台",
    "广州",
    "大连",
    "贵阳",
    "长沙",
    "杭州",
    "舟山",
    "曲阜",
    "宜昌",
    "诸暨",
    "延边",
    "桐乡",
    "阜新",
    "常州"
]

# 全季诸暨国际珠宝城酒店 8915743

month = '0909'
date = '0103'
params = {
    'checkInDate': '2023-'+month[:2]+'-'+date[:2],
    'checkOutDate': '2023-'+month[-2:]+'-'+date[-2:],
    'hotelId': '2013157',
}

hotelList = get_data(request_url, params, constant.headers)

list = []
city = hotelList['content']['cityName']
# booked = city in alreadyBook
print(json.dumps(hotelList['content']['hotelName']+' ' +
      hotelList['content']['hotelId'], ensure_ascii=False, indent=4).encode('utf-8'))
for item in hotelList['content']['roomPriceList']['roomList']:
    if item['isRoomOpenResv'] == True:
        bb = str(item['ratePlanCodeList']
                 [0]['dailyPrice'][0]['prices'][0]['marketPrice']*0.88*1.03)
        orgPrice = item['ratePlanCodeList'][0]['dailyPrice'][0]['prices'][0]['amount']
        price = int(math.ceil(orgPrice+10 if orgPrice <
                    300 else orgPrice*1.033))
        
        list.append(item['typeRoomName']+' ' +
                    str(price) + ' ' + item['hasWindow'])

# data = [{
#     'typeRoomName': item['typeRoomName'],
#     # 'roomArea': item['roomArea'],
#     'amount': item['ratePlanCodeList'][0]['dailyPrice'][0]['prices'][0]['amount'],
#     # 'marketPrice': item['ratePlanCodeList'][0]['dailyPrice'][0]['prices'][0]['marketPrice'],
#     # 'isRoomOpenResv': item['isRoomOpenResv'],
#     # 'price': item['ratePlanCodeList'][0]['dailyPrice'][0]['prices'][0]['amount']*0.85,
#     # 'hasWindow': item['hasWindow'],
#     # 'bedSize': item['bedSize']
# } for item in hotelList['content']['roomPriceList']['roomList']]

print(json.dumps(list, ensure_ascii=False, indent=4).encode('utf-8'))
