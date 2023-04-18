# -*- coding: utf-8 -*-

import requests
import re
import json
import codecs
import os
import datetime
from bs4 import BeautifulSoup

def filter_empty(d):
    # print(d)
    return {k:v for k,v in d.items() if v}

def download_files(list):
    for item in list:
        url = 'https://data.eastmoney.com/report/zw_industry.jshtml?infocode={}'.format(item.get('infoCode'))
        
        # # 发送请求并获取页面内容
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # # 查找具有类名“pdf-link”的<a>标签，并获取其href属性
        pdf_link = soup.find('a', {'class': 'pdf-link'})
        pdf_url = pdf_link['href']

        print(pdf_url)

        # # 下载PDF文件并保存到指定文件夹
        pdf_response = requests.get(pdf_url)
        # folder_path = os.path.join('pdf', item.title)
        # if not os.path.exists(folder_path):
        #     os.makedirs(folder_path)
        # folder_name = item.get('publishDate')[:4]+'/'+
        folder_path = os.path.join(os.getcwd(), 'pdf')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_name = item.get('publishDate')+item.get('title').replace('/', '|')+'.pdf'
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'wb') as f:
            f.write(pdf_response.content)

def gen_json(data):
    json_str = json.dumps(data, ensure_ascii=False)
    # print(json_str)

    with codecs.open('data.json', 'w', encoding="utf-8") as f:
        f.write(json_str)

# 生成01到12的数组
month = ['%02d' % i for i in range(1, 13)]
years = [2017,2018,2019,2020,2021,2022]
year = 2017
# for year in years:
for m in month:
    request_url = 'https://reportapi.eastmoney.com/report/list?cb=datatable1376407&industryCode=420&pageSize=50&industry=*&rating=*&ratingChange=*&beginTime={}-{}-01&endTime={}-{}-31&pageNo=1&fields=&qType=1&orgCode=&rcode=&_=1681172756383'.format(year, m, year, m)
    response = requests.get(request_url)

    content = response.text
    pattern = r'^\w+\((.*)\)$'
    match = re.match(pattern, content)
    if match:
        json_data = match.group(1)
    data = json.loads(json_data, encoding='utf-8')
    # print(data.get('TotalPage'))
    parsed_data = [item for item in data.get('data') if item['attachPages'] <= 7]
    parsed_data2 = [filter_empty(item) for item in parsed_data]
    parsed_data3 = [{
        'attachPages': item['attachPages'], 
        'title': item['title'], 
        'publishDate': item['publishDate'][:11], 
        'researcher': item.get('researcher'), 
        'orgSName': item.get('orgSName'),
        'infoCode': item['infoCode']
        } for item in parsed_data2]

    download_files(parsed_data3)

    # gen_json(parsed_data3)

