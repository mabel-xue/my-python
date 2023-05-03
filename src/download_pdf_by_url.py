
# -*- coding: utf-8 -*-

import requests
import urllib
from bs4 import BeautifulSoup
from utils import download_pdf
import os
import requests

# def download_pdf(url, filename):
#     response = requests.get(url)
#     with open(filename, 'wb') as f:
#         f.write(response.content)
#     print(f"Successfully downloaded {filename}")

def get_list():
    request_url = 'https://ir.aboutamazon.com/feed/FinancialReport.svc/GetFinancialReportList?apiKey=BF185719B0464B3CB809D23926182246&LanguageId=1&reportTypes=Annual%20Report&reportSubType%5B%5D=Annual%20Report&reportSubTypeList%5B%5D=Annual%20Report&pageSize=-1&pageNumber=0&tagList=&includeTags=true&year=-1&excludeSelection=1'
    res = requests.get(request_url)
    result = res.json()['GetFinancialReportListResult']
    # print(result)
    return result


folder_path = os.path.join(os.getcwd(), 'yeara')
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
for item in get_list():
  for file in item['Documents']:
    file_path = os.path.join(folder_path, file['DocumentTitle'] + '.pdf')
    # print(file_path)
    download_pdf(file['DocumentPath'], file_path)
