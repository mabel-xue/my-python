# -*- coding: utf-8 -*-

import requests
import re
import json
import codecs
import os
import datetime
from bs4 import BeautifulSoup
import math

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
    # 登录后手动更新
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NDE3OTgzMiwiaWF0IjoxNjgyNDI0Mjg5fQ.HRgBCNhKh8Sm79Ku9fhp9GFgnT0grGaH9qEPI16HM2M",
    "cache-control": "no-cache",
    "client-type": "pc",
    "client-ver": "v2.0.14",
    "origin": "https://www.djyanbao.com",
    "pragma": "no-cache",
    "referer": "https://www.djyanbao.com/",
    "sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
}


def download_files(list):
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    folder_path = os.path.join(os.getcwd(), 'DJ '+current_time)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    for item in list:
        url = 'https://api.djyanbao.com/api/report/{}/download/info?action=view'.format(
            item.get('id'))
        # print(item.get('id'))
        response = requests.get(url, headers=headers)
        # print(response.json())
        # # 查找具有类名“pdf-link”的<a>标签，并获取其href属性
        pdf_url = response.json()['data']['fileUrl']

        # # 下载PDF文件并保存到指定文件夹
        pdf_response = requests.get(pdf_url)
        file_name = item.get('publishAt')[
            :10]+' '+item.get('title').replace('/', '|')+'.pdf'
        print(file_name)
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'wb') as f:
            f.write(pdf_response.content)


# 报告类型
TypeIds = {
    # 行业研究
    'industry': 10,
    # 公司研究
    'gs': 16,
    # 宏观策略
    'hgcl': 14,
}
# 特色标签
LabelIds = {
    # 深度研究
    'deep': 11
}


def get_list(params):
    request_url = 'https://api.djyanbao.com/api/report'
    response = requests.get(request_url, params={
        'page': params.get('page', 1),
        'limit': 50,
        'q': params.get('q'),
        'pageMoreThan': 20,
        'labelIds': LabelIds["deep"],
        'typeIds': TypeIds['industry'],
        # 'title'
        'publishAtBegin': '2023-01-01',
        'publishAtEnd': '2023-03-31'
    }, headers=headers)
    result = response.json()['data']
    return result


# 生成01到12的数组
# month = ['%02d' % i for i in range(1, 13)]
# years = [2018,2019,2020,2021,2022,2023]
# for year in years:
#     for m in month:
q = '银行'
data = get_list({
    'q': q,
})
#
for i in data['data']:
    print('页数:'+str(i['pageTotal'])+' '+i['title'].encode('utf-8'))
# total=data['meta']['itemCount']
# page_number=int(math.ceil(total/50.0))
# print('total page:'+str(page_number)+','+'total count:'+str(total))
# for i in range(1, page_number+1):
#     print('cur page:'+str(i))
#     data = get_list({
#         'q': q,
#         'page': i
#     })
    # download_files(data['data'])
