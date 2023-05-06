# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import pandas as pd
from utils import get_soup
import openpyxl
from openpyxl.styles.alignment import Alignment
from openpyxl.styles import Alignment
from openpyxl.styles import Font

def wrap_cell(sheet):
  for col in range(1, sheet.max_column + 1):
    cell = sheet.cell(row=2, column=col)
    cell.alignment = openpyxl.styles.Alignment(wrap_text=True)

def merge_cell(sheet):
  sheet.merge_cells(start_row=1, end_row=1, start_column=2, end_column=3)
  sheet.merge_cells(start_row=1, end_row=1, start_column=4, end_column=6)
  sheet.merge_cells(start_row=1, end_row=1, start_column=7, end_column=15)
  sheet.merge_cells(start_row=1, end_row=1, start_column=16, end_column=25)
  sheet.merge_cells(start_row=1, end_row=1, start_column=26, end_column=28)
  sheet.merge_cells(start_row=1, end_row=1, start_column=29, end_column=31)
  for col in range(2, sheet.max_column + 1):
    cell = sheet.cell(row=1, column=col)
    cell.alignment = Alignment(horizontal='center', vertical='center')

file_name="output2.xlsx"
# 对比数据
codes=[{
  "name": '青岛啤酒',
  "code": '600600'
},{
  "name": '重庆啤酒',
  "code": '600132'
},{
  "name": '珠江啤酒',
  "code": '002461'
},{
  "name": '惠泉啤酒',
  "code": '600573'
},{
  "name": '燕京啤酒',
  "code": '000729'
},{
  "name": '兰州黄河',
  "code": '000929'
}]
vs_df=None
writer = pd.ExcelWriter(file_name, engine='openpyxl')

for item in codes:
  #
  url = 'https://caibaoshuo.com/companies/{}/financials'.format(item['code'])
  div = get_soup(url).find('div', {'id': 'alkey-yearly'})
  table = div.find('table')
  df = pd.read_html(str(table), encoding='utf-8')[0]
  # print(df)
  #
  if vs_df is None or vs_df.empty:
    vs_df = df.iloc[:, 0:2].copy()
  vs_df[item['name'].decode('utf-8')]=df['2022']

  # print(vs_df)
  # 删除 趋势 列
  del df[df.columns[2]]
  df.to_excel(writer, sheet_name=item['name'].decode('utf-8'), index=False)

vs_df = vs_df.transpose()
vs_df = vs_df.reset_index()
# vs_df.index.name = None
vs_df.to_excel(writer, sheet_name='vs', index=False, header=False)


# change sheet index
wb = writer.book
sheets = wb.sheetnames
if 'vs' in sheets:
    sheet_index = sheets.index('vs')
    sheets.insert(0, sheets.pop(sheet_index))
wb._sheets = [wb[sheet_name] for sheet_name in sheets]

writer.save()

# 打开 Excel 文件
book = openpyxl.load_workbook(file_name)

# 获取 vs sheet
vs_sheet = book['vs']

wrap_cell(vs_sheet)

merge_cell(vs_sheet)

# set th bold
for row in vs_sheet.iter_rows(min_row=1, max_row=1):
    for cell in row:
        cell.font = Font(bold=True)

# 保存文件
book.save(file_name)
