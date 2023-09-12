# -*- coding: utf-8 -*-

import json
from utils import get_data, calculate_date_range
import constant
import math

request_url = 'https://hweb-hotel.huazhu.com/hotels/hotel/detail'

alreadyBook = {
    '北京': {'0923'},
    '天津': {'1014'},
    '杭州': {'0915', '0916', '1004'},
    '连云港': {'0927'},
    '济南': {'0926', '1005'},
    '乌鲁木齐': {'0919'},
    '长沙': {'0916'},
    '威海': {'0912', '0924', '0925', '0926', '0927'},
    '南京': {'0913', '1006', '1007'},
    '桂林': {'0912'},
    '香格里拉': {'1017', '1018'},
    '珠江': {'0920', '0921', '0926', '0927', '0928'},
    '深圳': {'0913'},
}
# 诸暨 12-14
# 汕头 13
# 延边 15 16
# 桐乡 16
# 阜新 30-1005
# 常州 1006

# 全季诸暨国际珠宝城酒店 8915743

month = '0909'
date = '1417'
params = {
    'checkInDate': '2023-'+month[:2]+'-'+date[:2],
    'checkOutDate': '2023-'+month[-2:]+'-'+date[-2:],
    'hotelId': '9015925',
}

hotelList = get_data(request_url, params, constant.headers)

list = []
booked = False
str_city = str(hotelList['content']['cityName'].encode('utf-8'))
for day in calculate_date_range(month, date):
    if str_city in alreadyBook and day in alreadyBook.get(str_city):
        booked = True
        break
print(json.dumps(hotelList['content']['hotelName']+' ' +
      hotelList['content']['hotelId'] + ' ' + str(booked), ensure_ascii=False, indent=4).encode('utf-8'))
for item in hotelList['content']['roomPriceList']['roomList']:
    if item['isRoomOpenResv'] == True:
        amount = 0
        for price_item in item['ratePlanCodeList'][0]['dailyPrice']:
            amount = price_item['prices'][0]['amount'] + amount
        # orgPrice = item['ratePlanCodeList'][0]['dailyPrice'][0]['prices'][0]['amount']
        orgPrice = int(math.ceil(amount/len(item['ratePlanCodeList'][0]['dailyPrice'])))
        price = int(math.ceil(orgPrice+10 if orgPrice <
                    330 else orgPrice*1.04))
        # zc = ' 双早+'+ int(math.ceil(float(price)*0.29)) if booked else '双早'
        # print(str(zc))
        list.append(item['typeRoomName']+' ' +
                    str(price) + ' '+ item['hasWindow'])

for item in list:
    print(item)
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

# print(json.dumps(list, ensure_ascii=False, indent=4).encode('utf-8'))
