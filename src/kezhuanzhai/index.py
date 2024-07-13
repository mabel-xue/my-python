# 可转债筛选池
import akshare as ak
import pandas as pd
from datetime import datetime
from cash import get_cash_data


def output_excel(df):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f'kzz_{timestamp}.xlsx'
    df.to_excel(output_file, index=False)


bond_zh_cov_df = ak.bond_cb_jsl(cookie='kbz_newcookie=1; kbzw__Session=3kb0dab06es946vbbj6aemevd5; Hm_lvt_164fe01b1433a19b507595a43bf58262=1719233983,1719324706; HMACCOUNT=26BD2E5A129E88F1; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1720621107; kbzw__user_login=7Obd08_P1ebax9aX5MPYxuPv6N2Cq47k2ujc8NvpxtS-oqum3sLUla3frsuxn6rIppaqr6erlqLH2q-rzrLS28ingrKk6OHFzr6fqqagrKCrl5ecpLjH1r6bkqurpZ-rnaiTq4KypMi5v82Mwejv0uXY2JGrj6eXm8XC08ri7eTc4aeXq-TV3OOTxcLTgcPMlcGZnafBp5bWrpyYouDR4N7Mztu34NallqquoauXkIm_wcm2xZiXzt_M3Je63cTb0J2ZuNHr2-THpZKpraGoj6CPpJnIyt_N6cullqquoauX')
if len(bond_zh_cov_df) < 40:
    raise Exception("请更新集思录cookie！")
# bond_zh_cov_df = bond_zh_cov_df[bond_zh_cov_df['信用评级'].isin(
#     ['AAA', 'AA+']) & (bond_zh_cov_df['正股价'] > 5) & (bond_zh_cov_df['债现价'] < 115) & (bond_zh_cov_df['债现价'] < 115)]
# bond_zh_cov_df = bond_zh_cov_df[bond_zh_cov_df['债券评级'].isin(
#     ['AAA', 'AA+']) &
#     (bond_zh_cov_df['正股价'] > 5)]

# 过滤可转债
bond_zh_cov_df = bond_zh_cov_df[
    bond_zh_cov_df['债券评级'].isin(['AAA', 'AA+']) &
    (bond_zh_cov_df['正股价'] > 5) &
    (bond_zh_cov_df['现价'] < 116) &
    (bond_zh_cov_df['转股溢价率'] < 80) &
    pd.notnull(bond_zh_cov_df['回售触发价'])].sort_values(by='剩余年限', ascending=True)

# 合并现金表
codes = bond_zh_cov_df['正股代码']
cash_df = get_cash_data(codes)
print(cash_df)
bond_zh_cov_df = pd.merge(bond_zh_cov_df, cash_df,
                          on='正股代码', how='inner').drop_duplicates()

# 自定义计算1
bond_zh_cov_df['资产/余额'] = ((bond_zh_cov_df['期末现金及现金等价物余额']).astype(float) /
                           bond_zh_cov_df['剩余规模']).round(2)
bond_zh_cov_df = bond_zh_cov_df[bond_zh_cov_df['资产/余额'] > 0.7]

# 简化
selected_columns = [
    '代码',
    '转债名称',
    '现价',
    '涨跌幅',
    '正股代码',
    '正股名称',
    '正股价',
    '正股涨跌',
    '正股PB',
    '转股溢价率',
    '转债占比',
    '到期时间',
    '剩余年限',
    '剩余规模',
    '资产/余额'
]
bond_zh_cov_df = bond_zh_cov_df.loc[:, selected_columns]

print(bond_zh_cov_df)
output_excel(bond_zh_cov_df.sort_values(by="到期时间"))

#
