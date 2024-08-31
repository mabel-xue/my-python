# 强赎机会表
import akshare as ak
import pandas as pd
from datetime import datetime
from cash import get_cash_data
from utils import get_jsl_cookie, output_excel

df = ak.bond_cov_comparison()

# 过滤可转债
df = df[(df["正股最新价"] != "-")]
df = df[(df["转债最新价"] != "-")]
df = df[
    (df["正股最新价"].astype(float) > df["转股价"].astype(float))
    & (df["转债最新价"].astype(float) < 116.0)
]
print(len(df))
df["价格差"] = df["正股最新价"].astype(float) - df["转股价"].astype(float)
df["价差比"] = (
    (df["正股最新价"].astype(float) / df["转股价"].astype(float)) - 1
) * 100.0
df = df.sort_values(by="价差比", ascending=False)

# 简化
selected_columns = [
    "转债代码",
    "转债名称",
    "转债最新价",
    "正股代码",
    "正股名称",
    "价差比",
    "价格差",
    "正股最新价",
    "转股价",
    "上市日期",
]
df = df.loc[:, selected_columns]

print(df)
output_excel(df, "强赎机会表")
