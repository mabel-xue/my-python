# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import pandas as pd
from utils import get_soup

# 指定对比
codes=[{
  "name": 'ssjc',
  "code": '000089'
},{
  "name": 'shjc',
  "code": '600009'
}]
new_df=None
writer = pd.ExcelWriter('output2.xlsx', engine='openpyxl')
for item in codes:
  #
  url = 'https://caibaoshuo.com/companies/{}/financials'.format(item['code'])

  div = get_soup(url).find('div', {'id': 'alkey-yearly'})
  table = div.find('table')

  df = pd.read_html(str(table), encoding='utf-8')[0]
  # print(df)
  #
  if new_df is None or new_df.empty:
    new_df = grouped.iloc[:, 0:2].copy()
  new_df[item['name']]=df['2022']
  # print(new_df)
  del df[df.columns[2]]
  df.to_excel(writer, sheet_name=item['name'], index=False)

new_df.to_excel(writer, sheet_name='vs', index=False)
# change sheet index
wb = writer.book
sheets = wb.sheetnames
if 'vs' in sheets:
    sheet_index = sheets.index('vs')
    sheets.insert(0, sheets.pop(sheet_index))
wb._sheets = [wb[sheet_name] for sheet_name in sheets]

writer.save()