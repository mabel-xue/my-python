# -*- coding: utf-8 -*-

import json
from utils import get_data
import constant
import math

request_url = 'https://hweb-hotel.huazhu.com/hotels/hotel/detail'

month = '0910'
date = '3001'
params = {
    'checkInDate': '2023-'+month[:2]+'-'+date[:2],
    'checkOutDate': '2023-'+month[-2:]+'-'+date[-2:],
    'hotelId': '9012213',
}

hotelList = get_data(request_url, params, constant.headers)

list = []
print(hotelList['content']['hotelName'])
for item in hotelList['content']['roomPriceList']['roomList']:
    if item['isRoomOpenResv'] == True:
        bb = str(item['ratePlanCodeList']
                 [0]['dailyPrice'][0]['prices'][0]['marketPrice']*0.88*1.03)
        orgPrice = item['ratePlanCodeList'][0]['dailyPrice'][0]['prices'][0]['amount']
        price = int(math.ceil(orgPrice+10 if orgPrice <
                    320 else orgPrice*1.033))
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
