# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# 发送 GET 请求，获取 PDF 文件的 URL
# url = 'https://api.fxbaogao.com/mofoun/report/searchReport/search'
# params = {
#   "order": "2",
#   "pdfPage": "-1",
#   "pageNum": 1,
#   "pageSize": 20,
#   "paragraphSize": 3,
#   "keywords": "tiktok"
# }
# response = requests.post(url,params=params)
# soup = BeautifulSoup(response.text, 'html.parser')
# pdf_url = soup.find('canvas')['data-pdf-url']
# result=response.json()
# print(result['data'])
# 发送 GET 请求，获取 PDF 文件的二进制数据
# pdf_response = requests.get(pdf_url)

# 将二进制数据保存为 PDF 文件
# with open('output.pdf', 'wb') as f:
#     f.write(pdf_response.content)
import requests
import json

# 设置请求参数
url = 'https://api.fxbaogao.com/mofoun/report/searchReport/search'
data = {
    'data': {
        'keywords': 'tiktok',  # 搜索关键词
        # 'isExact': False,  # 是否精确匹配
        # 'pageNum': 1,  # 搜索结果页数
        # 'pageSize': 20,  # 搜索结果每页数量
        # 'orderBy': 'createdDate',  # 搜索结果排序字段
        # 'order': 'desc',  # 搜索结果排序方式
        # 'cate': '1',  # 报告类别
        # 'rpCate': '1',  # 报告行业
        # 'year': '2022',  # 报告年份
        # 'isTop': False,  # 是否置顶
        # 'isHot': False,  # 是否热门
        # 'isPrice': False,  # 是否付费
        # 'range': 'month',  # 时间范围
    }
}

# 发送 POST 请求
response = requests.post(url, json=data)

# 处理响应
if response.ok:
    result = json.loads(response.text)
    print(result)
    # 处理搜索结果
else:
    print('请求失败：', response.status_code)
