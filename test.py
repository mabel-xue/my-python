import akshare as ak
import pandas as pd

# 设置显示所有列
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

bond_zh_cov_df = ak.bond_zh_cov()
# 后10行
print(bond_zh_cov_df.tail(10).to_string(index=False))


# bond_cb_jsl_df = ak.bond_cb_jsl(
#     cookie="kbzw__Session=3kb0dab06es946vbbj6aemevd5; HMACCOUNT=26BD2E5A129E88F1; kbz_newcookie=1; Hm_lvt_164fe01b1433a19b507595a43bf58262=1721920140; kbzw__user_login=7Obd08_P1ebax9aX5MPYxuPv6N2Cq47k2ujc8NvpxtS-oqum3sLUla3frsuxn6rIppaqr6erlqLH2q-rzrLS28ingrKk6OHFzr6fqqagrKCrl5ecpLjH1r6bkqurp5mwoquZrYKypMi5v82Mwejv0uXY2JGrj6eXm8XC08ri7eTc4aeXq-TV3OOTxcLTgcPMlcGZnafBp5bWrpyYouDR4N7Mztu34NallqquoauXkIm_wcm2xZiXzt_M3Je63cTb0J2ZuNHr2-THpZKpraGoj6CPpJnIyt_N6cullqquoauX; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1722164181"
# )
# print(bond_cb_jsl_df)
