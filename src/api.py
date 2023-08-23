# -*- coding: utf-8 -*-

import requests

from utils import get_soup

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

def post_data(url, params=None, headers=None):
    try:
        response = requests.post(url, params=params, headers=headers)
        return handle_res(response)
    except requests.exceptions.RequestException as e:
        # 处理请求异常
        print(e)

# 某一行业下的股票列表(东方财富)
# np: 1 (jsonArray格式)
# pn: 1 (offset)
# pz: 965 (limit)
# fs: 股票/行业代码 如股票 b:BK0477 (b:是固定值) 如行业 m:90+t:2 (固定值)
# fields: f12,f14 (代码,名称)
# fid: 按什么排序 - f21 流通市值
# po: 0 升序 1 降序
def get_dongfang_stocks(industryCode):
    result=get_data('https://push2.eastmoney.com/api/qt/clist/get?pz=20&pn=1&np=1&fs={}&fields=f12,f14&fid=f21&po=1'.format(industryCode))
    data=[]
    for item in result['data']['diff']:
        print(item['f14'])
        data.append({
            'code': item['f12'],
            'name': item['f14'].encode('utf-8'),
        })
    return data

# 某一行业下的股票列表(财报说)
def get_caibaoshuo_stocks(industryCode,header=None):
    url = 'https://caibaoshuo.com/cn_industries/{}'.format(industryCode)
    div = get_soup(url, header=header).find('div', {'class': 'fullscreen-body'})
    tds=div.find('tbody').find_all('td', {'class': 'company-name-td'})

    data=[]
    for td in tds:
        print(td.find('a').text)
        obj={
            'name': td.find('a').text.encode('utf-8'),
            'code': td.find('span').text
        }
        data.append(obj)
    return data