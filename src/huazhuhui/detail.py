# -*- coding: utf-8 -*-

import json
from utils import get_data, calculate_date_range
import constant
import math

request_url = 'https://hweb-hotel.huazhu.com/hotels/hotel/detail'

alreadyBook = {
    '北京': {'0923'},
    '青岛': {'0923'},
    '广州': { '0926', '0927'},
    '珠江': {'0926', '0927', '0928'},
    '济南': {'0926', '1005'},
    '连云港': {'0927'},
    '杭州': {'0928', '1004'},
    '上海': {'0928','1001', '1002', '1004', '1013', '1014'},
    '洛阳': {'0929', '0930'},
    '长沙': {'1001', '1002'},
    '南京': { '1006', '1007'},
    '天津': {'1014'},
    '香格里拉': {'1017', '1018'},
}
# 丽水 23
# 昆明 24 7
# 阜新 30-5
# 兰州 2
# 赤峰 2 3 4
# 常州 6

# 全季诸暨国际珠宝城酒店 8915743


month = '1010'
date = '0406'
params = {
    'checkInDate': '2023-'+month[:2]+'-'+date[:2],
    'checkOutDate': '2023-'+month[-2:]+'-'+date[-2:],
    'hotelId': '9017108',
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
