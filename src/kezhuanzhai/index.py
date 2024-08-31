# 可转债筛选池
import akshare as ak
import pandas as pd
from datetime import datetime
from cash import get_cash_data
from utils import get_jsl_cookie, output_excel

cookie = "kbzw__Session=3kb0dab06es946vbbj6aemevd5; HMACCOUNT=26BD2E5A129E88F1; kbz_newcookie=1; Hm_lvt_164fe01b1433a19b507595a43bf58262=1721920140; kbzw__user_login=7Obd08_P1ebax9aX5MPYxuPv6N2Cq47k2ujc8NvpxtS-oqum3sLUla3frsuxn6rIppaqr6erlqLH2q-rzrLS28ingrKk6OHFzr6fqqagrKCrl5ecpLjH1r6bkqurp5mwoquZrYKypMi5v82Mwejv0uXY2JGrj6eXm8XC08ri7eTc4aeXq-TV3OOTxcLTgcPMlcGZnafBp5bWrpyYouDR4N7Mztu34NallqquoauXkIm_wcm2xZiXzt_M3Je63cTb0J2ZuNHr2-THpZKpraGoj6CPpJnIyt_N6cullqquoauX; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1722076479"
bond_zh_cov_df = ak.bond_cb_jsl(cookie=cookie)
if len(bond_zh_cov_df) < 40:
    raise Exception("请更新集思录cookie！")
# while len(bond_zh_cov_df) < 40:
#     jsl_cookie = get_jsl_cookie()
#     print("cookie 已更新", jsl_cookie)
#     bond_zh_cov_df = ak.bond_cb_jsl(cookie=jsl_cookie)
#     print("cookie 已更新2", len(bond_zh_cov_df))

# bond_zh_cov_df = bond_zh_cov_df[bond_zh_cov_df['信用评级'].isin(
#     ['AAA', 'AA+']) & (bond_zh_cov_df['正股价'] > 5) & (bond_zh_cov_df['债现价'] < 115) & (bond_zh_cov_df['债现价'] < 115)]
# bond_zh_cov_df = bond_zh_cov_df[bond_zh_cov_df['债券评级'].isin(
#     ['AAA', 'AA+']) &
#     (bond_zh_cov_df['正股价'] > 5)]

codes = ["123203"]  # 	明电转02
# 过滤可转债
bond_zh_cov_df = bond_zh_cov_df[
    bond_zh_cov_df["代码"].isin(codes)
    | (
        bond_zh_cov_df["债券评级"].isin(["AAA", "AA+"])
        & (bond_zh_cov_df["正股价"] > 5)
        & (bond_zh_cov_df["现价"] < 115)
        & (bond_zh_cov_df["转股溢价率"] < 80)
        & pd.notnull(bond_zh_cov_df["回售触发价"])
    )
].sort_values(by="剩余年限", ascending=True)

# 合并现金表
codes = bond_zh_cov_df["正股代码"]
cash_df = get_cash_data(codes)
print(cash_df)
bond_zh_cov_df = pd.merge(
    bond_zh_cov_df, cash_df, on="正股代码", how="inner"
).drop_duplicates()

# 自定义计算1
bond_zh_cov_df["资产/余额"] = (
    (bond_zh_cov_df["期末现金及现金等价物余额"]).astype(float)
    / bond_zh_cov_df["剩余规模"]
).round(2)
# bond_zh_cov_df = bond_zh_cov_df[bond_zh_cov_df["资产/余额"] > 0.7]

# 简化
selected_columns = [
    "代码",
    "转债名称",
    "现价",
    "涨跌幅",
    "正股代码",
    "正股名称",
    "正股价",
    "正股涨跌",
    "正股PB",
    "转股溢价率",
    "转债占比",
    "到期时间",
    "剩余年限",
    "剩余规模",
    "资产/余额",
]
bond_zh_cov_df = bond_zh_cov_df.loc[:, selected_columns]
bond_zh_cov_df = bond_zh_cov_df[~bond_zh_cov_df["代码"].isin(["110062", "127022"])]

print(bond_zh_cov_df)
output_excel(bond_zh_cov_df.sort_values(by="到期时间"), "过滤")

# 晶能转债 < 90 +
