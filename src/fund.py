# -*- coding: utf-8 -*-

# 功能说明：持仓基金在近5个工作日内净值累增减情况

# 导入需要的模块
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
import json
from datetime import datetime
from datetime import date, timedelta
import time

# 抓取网页
def get_url(url, params=None, proxies=None):
    rsp = requests.get(url, params=params, proxies=proxies)
    rsp.raise_for_status()
    return rsp.text

# 从网页抓取数据
def get_fund_data(code,per=10,sdate='',edate='',proxies=None):
    url = 'http://fund.eastmoney.com/f10/F10DataApi.aspx'
    params = {'type': 'lsjz', 'code': code, 'page':1,'per': per, 'sdate': sdate, 'edate': edate}
    html = get_url(url, params, proxies)
    soup = BeautifulSoup(html, 'html.parser')

    # 获取总页数
    pattern=re.compile(r'pages:(.*),')
    result=re.search(pattern,html).group(1)
    pages=int(result)

    # 获取表头
    heads = []
    for head in soup.findAll("th"):
        heads.append(head.contents[0])

    # 数据存取列表
    records = []

    # 从第1页开始抓取所有页面数据
    page=1
    while page<=pages:
        params = {'type': 'lsjz', 'code': code, 'page':page,'per': per, 'sdate': sdate, 'edate': edate}
        html = get_url(url, params, proxies)
        soup = BeautifulSoup(html, 'html.parser')

        # 获取数据
        for row in soup.findAll("tbody")[0].findAll("tr"):
            row_records = []
            for record in row.findAll('td'):
                val = record.contents

                # 处理空值
                if val == []:
                    row_records.append(np.nan)
                else:
                    row_records.append(val[0])

            # 记录数据
            records.append(row_records)

        # 下一页
        page=page+1

    # 数据整理到dataframe
    np_records = np.array(records)
    data= pd.DataFrame()
    for col,col_name in enumerate(heads):
        data[col_name] = np_records[:,col]

    return data

def get_fund_info(code):
    url = 'https://fundgz.1234567.com.cn/js/{}.js?v=20200908175500'.format(code)
    # time.sleep(3)
    response = requests.get(url)

    # 提取响应内容中的JSON字符串
    json_str = response.content.decode('utf-8').split('jsonpgz(')[1].split(');')[0]
    if (json_str):
      # 将JSON字符串转换为Python对象
      data = json.loads(json_str)
      name = data['name']
      return name
    
    nameMap = {
      '008763': '天弘越南市场股票',
      '161127': '易方达标普生物科技人民币',
      '006289': '华夏养老2040三年'
    }
    return  nameMap.get(code, '')

funds = pd.DataFrame()

# 主程序
if __name__ == "__main__":
    today = datetime.now().strftime('%Y-%m-%d')
    seven_days_ago = date.today() - timedelta(days=9)
    seven_days_ago_str = seven_days_ago.strftime('%Y-%m-%d')
    codes = [
        "163402","163406","003133","110035","340001","002351","007345","014412","161029","012894","001629",
        "001594","008763","004818","014331","161907","008283","005662","006228","010409","010557","160218",
        "161127","167301","673100","001018","000592","005535","002943","000251","167506","000793","006289"
        ]
    for code in codes:
      df=get_fund_data(code,per=20,sdate=seven_days_ago_str,edate=today)
      # 修改数据类型
      df.drop(df.columns[-3:], axis=1, inplace=True) # 删除后三列
      df.drop(columns=[u'单位净值',u'累计净值',u'净值日期'], inplace=True)
      name = get_fund_info(code)
      df['name']=name
      df['fundcode']=code
      df['rate']=df[u'日增长率'].str.strip('%').astype(float) / 100
      df['lzld'] = df['rate'].head(5).sum()
      df.drop(columns=['rate'], inplace=True)
      df['lzld'] = (df['lzld'] * 100)
      if df.empty:
        funds = pd.DataFrame(columns=df.columns)
      funds = funds.append(df.iloc[0])
    
    funds=funds.sort_values(by='lzld',axis=0,ascending=True).reset_index(drop=True)
    # funds.style.format({'name': '', '单位净值': '{:.4f}', '累计净值': '{:.4f}', '日增长率': '{:.2%}'})
    print(funds)

    # data['净值日期']=pd.to_datetime(data['净值日期'],format='%Y/%m/%d')
    # data['单位净值']= data['单位净值'].astype(float)
    # data['累计净值']=data['累计净值'].astype(float)
    # data['日增长率']=data['日增长率'].str.strip('%').astype(float)
    # # 按照日期升序排序并重建索引
    # data=data.sort_values(by='净值日期',axis=0,ascending=True).reset_index(drop=True)
