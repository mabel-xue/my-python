# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def download_pdf(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    print("Successfully downloaded" + filename)


# 从html抓取数据


def get_soup(url, header=None):
    # url = 'https://caibaoshuo.com/companies/{}/financials'.format(code)
    rsp = requests.get(url, headers=header)
    rsp.raise_for_status()
    html = rsp.text
    soup = BeautifulSoup(html, "html.parser")
    return soup


# 类似可选链


def get_nested_value(obj, keys):
    try:
        for key in keys:
            obj = obj[key]
        return obj
    except (TypeError, KeyError, IndexError):
        return None


jsl_cookie = "kbz_newcookie=1; kbzw__Session=3kb0dab06es946vbbj6aemevd5; Hm_lvt_164fe01b1433a19b507595a43bf58262=1719233983,1719324706; HMACCOUNT=26BD2E5A129E88F1; kbzw__user_login=7Obd08_P1ebax9aX5MPYxuPv6N2Cq47k2ujc8NvpxtS-oqum3sLUla3frsuxn6rIppaqr6erlqLH2q-rzrLS28ingrKk6OHFzr6fqqagrKCrl5ecpLjH1r6bkqurppyqnK6Wp4KypMi5v82Mwejv0uXY2JGrj6eXm8XC08ri7eTc4aeXq-TV3OOTxcLTgcPMlcGZnafBp5bWrpyYouDR4N7Mztu34NallqquoauXkIm_wcm2xZiXzt_M3Je63cTb0J2ZuNHr2-THpZKpraGoj6CPpJnIyt_N6cullqquoauX; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1721310742"
