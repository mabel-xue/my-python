# -*- coding: utf-8 -*-

import json
from utils import get_data, calculate_date_range
import constant
import math

request_url = 'https://hweb-hotel.huazhu.com/hotels/hotel/detail'

alreadyBook = {
    '青岛': {'1014'},
    '广州': { '1019', '1010', '1011', '1012'},
    '上海': {'1013', '1014'},
    '天津': {'1014'},
    '香格里拉': {'1016', '1017'},
    '哈尔滨': {'1017', '1018'},
    '杭州': {'1103', '1117'},
    '长沙': {'1017'}
}

# 深圳 10

# 全季诸暨国际珠宝城酒店 8915743


month = '1010'
date = '1011'
params = {
    'checkInDate': '2023-'+month[:2]+'-'+date[:2],
    'checkOutDate': '2023-'+month[-2:]+'-'+date[-2:],
    'hotelId': '8915511',
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
        if str(item['ratePlanCodeList'][0]['mealPlanSummary'].encode('utf-8')) == '2份早餐':
            for price_item in item['ratePlanCodeList'][0]['dailyPrice']:
                amount = price_item['prices'][0]['amount'] + amount
            # orgPrice = item['ratePlanCodeList'][0]['dailyPrice'][0]['prices'][0]['amount']
            orgPrice = int(math.ceil(amount/len(item['ratePlanCodeList'][0]['dailyPrice'])))
            price = int(math.ceil(orgPrice+10 if orgPrice <
                        330 else orgPrice*1.038))
            list.append(item['typeRoomName']+' ' +
                        str(price) + ' '+ item['hasWindow'])
        else:
            print('token 过期')

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
