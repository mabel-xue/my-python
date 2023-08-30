# -*- coding: utf-8 -*-

import json
from utils import get_data
import constant
import math

request_url = 'https://hweb-hotel.huazhu.com/hotels/hotel/detail'

alreadyBook = {
    '重庆': ['0830'],
    '济南': ['0902'],
    '洛阳': ['0902'],
    '西安': ['0831', '0901', '0902'],
    '阜新': ['0930', '1001', '1002', '1003',  '1004'],
    '淄博': ['0901'],
    '上海': ['0901', '0904', '0905'],
    '连云港': ['0902'],
    '烟台': ['0902', '0903'],
    '宜昌': ['0903'],
    '大连': ['0904', '0905', '0906', '0907'],
    '长沙': ['0915'],
    '延边': ['0915', '0916'],
    '杭州': ['1004']
}

month = '1010'
date = '0607'
params = {
    'checkInDate': '2023-'+month[:2]+'-'+date[:2],
    'checkOutDate': '2023-'+month[-2:]+'-'+date[-2:],
    'hotelId': '9008531',
}

hotelList = get_data(request_url, params, constant.headers)

list = []
city = hotelList['content']['cityName']
booked = True if city in alreadyBook.values() else False
print(hotelList['content']['hotelName']+' '+hotelList['content']['hotelId']+' '+str(booked))
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
