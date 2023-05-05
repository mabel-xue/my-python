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
dict_map_for_bank={
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
      # "title_1": "经营活动产生的现金流量",
      "deposit_and_interbank_net_add": "客户存款和同业存放款项净增加额",
      # "borrowing_net_add_central_bank": "向中央银行借款净增加额",
      # "lending_net_add_other_org": "向其他金融机构拆入资金净增加额",
      # "sub_total_of_ci_from_oa": "经营活动现金流入小计",
      # "cash_paid_to_employee_etc": "支付给职工以及为职工支付的现金",
      # "sub_total_of_cos_from_oa": "经营活动现金流出小计",

      
      "ncf_from_oa": "经营活动产生的现金流量",


      "ncf_from_ia": "投资活动产生的现金流量净额",
      "ncf_from_fa": "筹资活动产生的现金流量净额",
      "cash_received_of_othr_oa": "其他经营活动产生的现金流入额",
      "payments_of_all_taxes": "缴纳的各项税费",
      "othrcash_paid_relating_to_oa": "其他经营活动支付的现金",
      "cash_received_of_dspsl_invest": "处置固定资产、无形资产和其他长期资产所收回的现金净额",
      "invest_income_cash_received": "取得投资收益所收到的现金",
      "net_cash_of_disposal_assets": "处置固定资产、无形资产和其他长期资产所收到的现金净额",
      "net_cash_of_disposal_branch": "处置子公司及其他营业单位收到的现金净额",
      "cash_received_of_othr_ia": "其他投资活动产生的现金流入额",
      "sub_total_of_ci_from_ia": "投资活动现金流入小计",
      "invest_paid_cash": "购建固定资产、无形资产和其他长期资产所支付的现金",
      "cash_paid_for_assets": "购买固定资产、无形资产和其他长期资产所支付的现金",
      "othrcash_paid_relating_to_ia": "其他投资活动支付的现金",
      "sub_total_of_cos_from_ia": "投资活动现金流出小计",
      "cash_received_of_absorb_invest": "吸收投资所收到的现金",
      "cash_received_from_investor": "其中：子公司吸收少数股东投资收到的现金",
      "cash_received_from_bond_issue": "发行债券收到的现金",
      "cash_received_of_borrowing": "取得借款所收到的现金",
      "cash_received_of_othr_fa": "其他筹资活动产生的现金流入额",
      "sub_total_of_ci_from_fa": "筹资活动现金流入小计",
      "cash_pay_for_debt": "偿还债务所支付的现金",
      "cash_paid_of_distribution": "分配股利、利润或偿付利息所支付的现金",
      "branch_paid_to_minority_holder": "支付给少数股东的股利、利润或偿付利息所支付的现金",
      "othrcash_paid_relating_to_fa": "其他筹资活动支付的现金",
      "sub_total_of_cos_from_fa": "筹资活动现金流出小计",
      "effect_of_exchange_chg_on_cce": "汇率变动对现金及现金等价",
      "net_increase_in_cce": "经营活动产生的现金流量净额",
      "initial_balance_of_cce": "经营活动现金流量净额期初余额",
      "final_balance_of_cce": "经营活动现金流量净额期末余额",
      "cash_received_of_interest_etc": "利息收到的现金",
      "loan_and_advance_net_add": "放款及垫款净增加额",
      "naa_of_cb_and_interbank": "向中央银行和同业拆出资金净增加额",
      "cash_paid_for_interests_etc": "利息等费用支付的现金",
      "net_cash_amt_from_branch": "拆入资金净减少额"
   }
}


dict_map={
   "balance": {
        "currency_funds": "货币资金",
        "tradable_fnncl_assets": "交易性金融资产",
        'ar_and_br': '应收票据及应收账款',
        "bills_receivable": "其中：应收票据",
        "account_receivable": "应收账款",
        "pre_payment": "预付款项",
        "interest_receivable": "应收利息",
        "dividend_receivable": "应收股利",
        "othr_receivables": "其他应收款",
        "inventory": "存货",
        'contractual_assets': '合同资产',
        # 'to_sale_asset': '待售资产',
        'to_sale_asset': '划分为持有待售的资产',
        "nca_due_within_one_year": "一年内到期的非流动资产",
        "othr_current_assets": "其他流动资产",
        'total_current_assets': '流动资产合计',
        'salable_financial_assets': '可供出售金融资产',
        "held_to_maturity_invest": "持有至到期投资",
        'lt_receivable': '长期应收款',
        "lt_equity_invest": "长期股权投资",
        'other_eq_ins_invest': '其他权益工具投资',
        'other_illiquid_fnncl_assets': '其他非流动金融资产',
        "invest_property": "投资性房地产",
        'fixed_asset_sum': '固定资产合计',
        "fixed_asset": "其中：固定资产",
        'fixed_assets_disposal': '固定资产清理',
        'construction_in_process_sum': '在建工程合计',
        "construction_in_process": "在建工程",
        'project_goods_and_material': '工程物资',
        'productive_biological_assets': '生产性生物资产',
        'oil_and_gas_asset': '油气资产',
        "intangible_assets": "无形资产",
        'dev_expenditure': '开发支出',
        "goodwill": "商誉",
        'lt_deferred_expense': '长期待摊费用',
        "dt_assets": "递延所得税资产",
        'othr_noncurrent_assets': '其他非流动资产',
        'total_noncurrent_assets': '非流动资产合计',
        "total_assets": "资产合计",
        'current_liab_si': '流动负债',
        'st_loan': '短期借款',
        "tradable_fnncl_liab": "交易性金融负债",
        "derivative_fnncl_liab": "衍生金融负债",
        'bp_and_ap': '应付票据及应付账款',
        'bill_payable': '应付票据',
        'accounts_payable': '应付账款',
        'pre_receivable': '预收款项',
        'contract_liabilities': '合同负债',
        "payroll_payable": "应付职工薪酬",
        "tax_payable": "应交税费",
        "interest_payable": "应付利息",
        'dividend_payable': '应付股利',
        'othr_payables': '其他应付款',
        # 'to_sale_debt': '待售债券投资',
        'to_sale_debt': '划分为持有待售的负债',
        'noncurrent_liab_due_in1y': '一年内到期的非流动负债',
        'othr_current_liab': '其他流动负债',
        'total_current_liab': '流动负债合计',
        'noncurrent_liab_si': '非流动负债',
        'lt_loan': '长期借款',
        "bond_payable": "应付债券",
        'lt_payable_sum': '长期应付款合计',
        'lt_payable': '长期应付款',
        'special_payable': '专项应付款',
        "estimated_liab": "预计负债",
        "dt_liab": "递延所得税负债",
        # 'noncurrent_liab_di': '长期递延负债',
        'noncurrent_liab_di': '递延收益-非流动负债',
        'othr_non_current_liab': '其他非流动负债',
        'total_noncurrent_liab': '非流动负债合计',
        "total_liab": "负债合计",
        "shares": "实收资本(或股本)",
        "othr_equity_instruments": "其他权益工具",
        'perpetual_bond': '永续债',
        "capital_reserve": "资本公积",
        # "treasury_stock": "减资准备",
        "treasury_stock": "减：库存股",
        "othr_compre_income": "其他综合收益",
        'special_reserve': '专项储备'
        "earned_surplus": "盈余公积",
        "undstrbtd_profit": "未分配利润",
        "general_risk_provision": "一般风险准备",
        "frgn_currency_convert_diff": "外币报表折算差额",
        "total_quity_atsopc": "归属于母公司股东权益合计",
        "minority_equity": "少数股东权益",
        "total_holders_equity": "股东权益合计",
        "total_liab_and_holders_equity": "负债和股东权益总计",


        # "asset_liab_ratio": "资产负债率",
        # "saleable_finacial_assets": "持有待售的金融资产",
        # "current_assets_si": "流动资产特殊项目",
        # 'noncurrent_assets_si': '长期资产',
   },
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
 "ncf_from_oa": "经营活动产生的现金流量净额",
    "ncf_from_ia": "投资活动产生的现金流量净额",
    "ncf_from_fa": "筹资活动产生的现金流量净额",
    "cash_received_of_othr_oa": "经营活动中收到的其他与现金有关的项目",
    "sub_total_of_ci_from_oa": "经营活动现金流入小计",
    "cash_paid_to_employee_etc": "支付给职工以及为职工支付的现金",
    "payments_of_all_taxes": "缴纳的各种税费",
    "othrcash_paid_relating_to_oa": "经营活动中支付的其他与现金有关的项目",
    "sub_total_of_cos_from_oa": "经营活动现金流出小计",
    "cash_received_of_dspsl_invest": "处置投资收回的现金",
    "invest_income_cash_received": "投资收益中收到的现金",
    "net_cash_of_disposal_assets": "处置固定资产、无形资产和其他长期资产所收回的现金净额",
    "net_cash_of_disposal_branch": "处置子公司及其他营业单位收到的现金净额",
    "cash_received_of_othr_ia": "投资活动中收到的其他与现金有关的项目",
    "sub_total_of_ci_from_ia": "投资活动现金流入小计",
    "invest_paid_cash": "购建固定资产、无形资产和其他长期资产所支付的现金",
    "cash_paid_for_assets": "购建固定资产、无形资产和其他长期资产所支付的现金",
    "othrcash_paid_relating_to_ia": "投资活动中支付的其他与现金有关的项目",
    "sub_total_of_cos_from_ia": "投资活动现金流出小计",
    "cash_received_of_absorb_invest": "吸收投资所收到的现金",
    "cash_received_from_investor": "从股东那里吸收投资所收到的现金",
    "cash_received_from_bond_issue": "发行债券所收到的现金",
    "cash_received_of_borrowing": "取得借款所收到的现金",
    "cash_received_of_othr_fa": "筹资活动中收到的其他与现金有关的项目",
    "sub_total_of_ci_from_fa": "筹资活动现金流入小计",
    "cash_pay_for_debt": "偿还债务支付的现金",
    "cash_paid_of_distribution": "分配股利、利润或偿付利息所支付的现金",
    "branch_paid_to_minority_holder": "支付给少数股东的股利、利润",
    "othrcash_paid_relating_to_fa": "筹资活动中支付的其他与现金有关的项目",
    "sub_total_of_cos_from_fa": "筹资活动现金流出",
    'sub_total_of_cos_from_fa': '固定资产处置净收益',
    'effect_of_exchange_chg_on_cce': '现金及现金等价物的汇率变动金额',
    'net_increase_in_cce': '现金及现金等价物净增加额',
    'initial_balance_of_cce': '期初现金及现金等价物余额',
    'final_balance_of_cce': '期末现金及现金等价物余额',
    'cash_received_of_sales_service': '销售商品、提供劳务收到的现金',
    'refund_of_tax_and_levies': '支付的各项税费返还',
    'goods_buy_and_service_cash_pay': '购买商品、接受劳务支付的现金',
    'net_cash_amt_from_branch': '由经营活动产生的其他现金流量金额'
   }
}

def get_excel(name):
  # 遍历data,取数
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