# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def download_pdf(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print("Successfully downloaded" + filename)

# 从html抓取数据


def get_soup(url, header=None):
    # url = 'https://caibaoshuo.com/companies/{}/financials'.format(code)
    rsp = requests.get(url, headers=header)
    rsp.raise_for_status()
    html = rsp.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# 类似可选链


def get_nested_value(obj, keys):
    try:
        for key in keys:
            obj = obj[key]
        return obj
    except (TypeError, KeyError, IndexError):
        return None
