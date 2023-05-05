# -*- coding: utf-8 -*-

import requests
import json
import codecs
import os
def gen_json(data):
    json_str = json.dumps(data, ensure_ascii=False)
    # print(json_str)

    with codecs.open('data.json', 'w', encoding="utf-8") as f:
        f.write(json_str)

# Define the function to scrape data from a financial website

def get_and_download_pdf_flie(code):
    
    topSearch=requests.post('http://www.cninfo.com.cn/new/information/topSearch/query?keyWord={}&maxNum=10'.format(code))
    top_info=topSearch.json()
    url='http://www.cninfo.com.cn/new/hisAnnouncement/query'
    pageNum=int(1)
    print(code+','+top_info[0]['orgId'])
    data={
        'stock':code+','+top_info[0]['orgId'],
        'pageNum':pageNum,
        'pageSize':999,
        # 'column':'szse',
        'tabName':'fulltext',
        # 'plate':'sz', 
        'searchkey':'',
        'secid':'',
        'category':'category_ndbg_szsh;',
        'trade':'', 
        'sortName':'',
        'sortType':'', 
        'isHLtitle':'true'}
    headers={
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Content-Length':'181',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Host':'www.cninfo.com.cn',
        'Origin':'http://www.cninfo.com.cn',
        'Referer':'http://www.cninfo.com.cn/new/disclosure/stock?stockCode=000089&orgId=gssz0000089',
        }
    
    # Send a request to the website to get data
    res=requests.post(url,data=data)
    result=res.json()

    # Download the PDF files
    announcements=result['announcements']
    if announcements is not None:
        list = [item for item in announcements if item is not None and '摘要' not in item['announcementTitle'].encode('utf-8') and "2022" in item["announcementTitle"].encode('utf-8')]
    else:
        return
    # print(list)
    for item in list:
        pdf_url='http://static.cninfo.com.cn/'+item['adjunctUrl']
        pdf_response = requests.get(pdf_url)

        title = item['announcementTitle'].encode('utf-8')
        secName = item['secName'].encode('utf-8')
        folder_path = os.path.join(os.getcwd(), '年报')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_name = secName+'-'+title.replace('/', '|')+'.pdf'
        print(file_name)
        file_path = os.path.join(folder_path, file_name)
        with open(file_path,'wb') as f:
            f.write(pdf_response.content)


# 某一行业下的股票列表
# np: 1 (jsonArray格式)
# pn: 1 (offset)
# pz: 965 (limit)
# fs: 股票/行业代码 如股票 b:BK0477 (b:是固定值) 如行业 m:90+t:2 (固定值)
# fields: f12,f14 (代码,名称)
# url='https://push2.eastmoney.com/api/qt/clist/get'
url='https://push2.eastmoney.com/api/qt/clist/get?fid=f62&po=1&pz=50&pn=1&np=1&fltt=2&invt=2&ut=b2884a393a59ad64002292a3e90d46a5&fs=b%3ABK0473&fields=f12,f14'
res=requests.get(url)
result=res.json()
# print(result['data']['diff'])
#3.设置循环，下载多页的年报
for item in result['data']['diff']:
    # print(item['f12'])
    get_and_download_pdf_flie(item['f12'])