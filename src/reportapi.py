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

        print(file_name)

        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'wb') as f:
            f.write(pdf_response.content)

def gen_json(data):
    json_str = json.dumps(data, ensure_ascii=False)
    # print(json_str)

    with codecs.open('data.json', 'w', encoding="utf-8") as f:
        f.write(json_str)

IndustryCode = {
    # 文化传媒
    'whcm': 486,
    # 银行
    'yh': 475,
    # 公共事业
    'ggsy': 427,
    # 航空机场
    'hkjc': 420,
    # 房地产开发
    'fdckf': 451,
}

def get_report(params):
    # request_url = 'https://reportapi.eastmoney.com/report/list?cb=datatable1376407&industryCode=486&pageSize=100&industry=*&rating=*&ratingChange=*&beginTime={}-{}-01&endTime={}-{}-31&pageNo=1&fields=&qType=1&orgCode=&rcode=&_=1681172756383'.format(params.year, params.m, params.year, params.m)
    request_url = 'https://reportapi.eastmoney.com/report/list'

    response = requests.get(request_url, params={
        'cb':'datatable1143488',
        # 个股
        # 'code': 600332,
        # 行业
        'industryCode':IndustryCode['fdckf'],
        'pageSize':100,
        # 'industry':'*',
        # 'rating':'*',
        # 'ratingChange':'*',
        # 'beginTime':'{}-{}-01'.format(params.get('year'), params.get('month')),
        # 'endTime':'{}-{}-31'.format(params.get('year'), params.get('month')),
        # 指定时间
        'beginTime':'2023-01-01',
        'endTime':'2023-04-30',
        'pageNo':params.get('pageNo'),
        # 1 行业分析 0 个股分析
        'qType':1,
        # '_':'1681972161483'
    })

    content = response.text
    pattern = r'^\w+\((.*)\)$'
    match = re.match(pattern, content)
    if match:
        json_data = match.group(1)
    return json.loads(json_data, encoding='utf-8')

# 全量查询
# month = ['%02d' % i for i in range(1, 13)]
# years = [2018,2019,2020,2021,2022,2023]
# for year in years:
#     for m in month:
data = get_report({
    # 'year': year,
    # 'month': m,
    'pageNo': 1,
})
# print(data.get('TotalPage'))
l=0
if data.get('TotalPage') >= 1:
    for i in range(1, data.get('TotalPage')+1):
        data =   get_report({
            # 'year': year,
            # 'month': m,
            'pageNo': i
        })
        # print(data.get('TotalPage'))
        parsed_data = [item for item in data.get('data') if item['attachPages'] > 12]
        # parsed_data = data.get('data')
        # print(parsed_data)
        parsed_data2 = [filter_empty(item) for item in parsed_data]
        parsed_data3 = [{
            'attachPages': item['attachPages'],
            'title': item['title'],
            'publishDate': item['publishDate'][:11],
            'researcher': item.get('researcher'),
            'orgSName': item.get('orgSName'),
            'infoCode': item['infoCode']
            } for item in parsed_data2]
        l=l+len(parsed_data3)

        # 打印
#         parsed_data_deep = [item for item in parsed_data3 if item['attachPages'] > 25]
#         for i in parsed_data_deep:
#             print('页数:'+str(i['attachPages'])+' '+i['title'].encode('utf-8'))
# print(l)
        # 下载
        # download_files(parsed_data3)

        # gen_json(parsed_data3)