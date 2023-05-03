# -*- coding: utf-8 -*-

import requests
import pandas as pd

headers={
   "Cookie": "xq_is_login=1; u=4920007320; snbim_minify=true; amp_d915a9=W2IBeF7liMZxje8Tvb42r_.M2h6VHJVbFVEeVRYYWtSZXowQmJGSG9TZlp3Mg==..1ggkk8ahn.1ggknh05m.1.24.25; amp_adc4c4=pYvValF9AWYU5pFLodlZ9O.M2h6VHJVbFVEeVRYYWtSZXowQmJGSG9TZlp3Mg==..1gpnnddoh.1gpnndql1.0.k.k; bid=beb56d7f152e88993f326d57ae7793c0_lfe3jepu; device_id=b6149a8a71729a61ef59ffee3cce6986; s=ct12e06q6w; xq_a_token=323758feae7585b5ccfa3b8808a20c80beb72080; xqat=323758feae7585b5ccfa3b8808a20c80beb72080; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjQ5MjAwMDczMjAsImlzcyI6InVjIiwiZXhwIjoxNjg1MzIyMDYwLCJjdG0iOjE2ODI3MzAwNjAxMzYsImNpZCI6ImQ5ZDBuNEFadXAifQ.kZuQ8pBwkmub6j-shtyqBIz7E6w0iao_SjCo5xhl58fEKjlMjz3S472ZJ-uZ7h8gSHw0RU21RXpp_o30A6D9A-w0vjJ2zLH1YCkMgGkCLbhIhEdppNyrvb63T80SpIkyL4yGZTyggHViPg-IEscN5_7Lrfn90dl7VqUiisbFM_jEv1Q8bMbL3rFtPhEnVbXEvfAv2hsroj7U77Yzj5AoTDpQik7EMkzjDwlCN9ZyDTAgHuBdt2T46GjZe6ne1YxVaNyI5zU1wBcBqGocv1hsDpA0jjul6Euz_JPhsCQLqg19T7j7B4IYguZoJv5CevtfiTXh_90OMd2j_0UKTOKjmw; xq_r_token=f2bc7ceda8e2b6e3826913cadc96c407d44e823b; Hm_lvt_1db88642e346389874251b5a1eded6e3=1682730060; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1683087143",
   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

def get_list(request_url):
    # request_url = 'https://stock.xueqiu.com/v5/stock/finance/cn/income.json'
    res = requests.get(request_url, params={
        'symbol':'SH601166',
        'type':'Q4',
        'is_detail':'true',
        'count':99
    },headers=headers)
    result = res.json()['data']['list']
    # print(result)
    return result


dict_map={
   "balance": {},
   "income": {
      "total_revenue": "营业总收入",
      "interest_net_income": "利息净收入",
      "interest_income": "其中，利息收入",
      "interest_payout": "利息支出",
      "commi_net_income": "手续费及佣金净收入",
      "fee_and_commi_income": "其中：手续费及佣金收入",
      "charge_and_commi_expenses": "手续费及佣金支出",
      "invest_incomes_from_rr": "投资收益",
      "invest_income": "其中：对联营企业和合营企业的投资收益",
      "income_from_chg_in_fv": "公允价值变动收益",
      "exchg_gain": "汇兑收益",
      "othr_income": "其他业务收入",
      "operating_payout": "营业总成本",
      "operating_taxes_and_surcharge": "营业税金及附加",
      "business_and_manage_fee": "业务及管理费",
      "asset_impairment_loss": "资产减值损失",
      "credit_impairment_loss": "信用减值损失",
      "othr_business_costs": "其他业务成本",
      "op": "营业利润",
      "non_operating_income": "加：营业外收入",
      "non_operating_payout": "减：营业外支出",
      "profit_total_amt": "利润总额",
      "income_tax_expenses": "减：所得税费用",
      "net_profit": "净利润",
      "net_profit_atsopc": "归属于母公司股东的净利润",
      "minority_gal": "少数股东损益",
      "net_profit_after_nrgal_atsolc": "扣除非经常性损益后的净利润",
      "basic_eps": "基本每股收益",
      "dlt_earnings_per_share": "稀释每股收益",
      "othr_compre_income": "其他综合收益",
      "othr_compre_income_atoopc": "归属母公司所有者的其他综合收益",
      "othr_compre_income_atms": "归属于少数股东的其他综合收益）",
      "total_compre_income": "综合收益总额",
      "total_compre_income_atsopc": "归属于母公司股东的综合收益总额",
      "total_compre_income_atms": "归属于少数股东的综合收益总额",
   },
   "cash_flow": {
   
   }
}

def get_excel(name):
  # 遍历d ata,取数
  df_obj={}
  columns_order=[]
  request_url = 'https://stock.xueqiu.com/v5/stock/finance/cn/{}.json'.format(name)
  list=get_list(request_url)
  print(len(list))
  columns_order.append('科目')

  for key, value in dict_map[name].items():
      columns_order.append(value)
      dataArr=[]
      yearArr=[]
      for item in list:
          yearArr.append(item['report_name'])
          dataArr.append(item[key][0])
      df_obj['科目']=yearArr
      df_obj[value]=dataArr
  # print(df_obj)
  # 创建DataFrame对象
  df = pd.DataFrame(df_obj, columns=columns_order)
  print(df)
  # df = pd.DataFrame({'年份': ['张三', '李四', '王五'],
  #                    '年龄': [25, 30, 28],
  #                    '性别': ['男', '男', '女']})

  # 创建Excel写入器
  writer = pd.ExcelWriter('output.xlsx', engine='openpyxl')

  # 翻转DataFrame的横纵轴
  df = df.transpose()

  # 重新设置表头
  df = df.reset_index()

  # 将DataFrame写入Excel文件
  df.to_excel(writer, sheet_name=name, index=False)

  # 保存Excel文件
  writer.save()

data=['income']
# data=['balance','income','cash_flow']
for item in data:
  get_excel(item)