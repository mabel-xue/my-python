import akshare as ak
import pandas as pd
from datetime import datetime


def get_cash_data(stock_symbols):
    result = []
    for symbol in stock_symbols:
        stock_financial_analysis_indicator_df = ak.stock_financial_analysis_indicator(
            symbol=symbol, start_year="2019")
        # print(
        #     stock_financial_analysis_indicator_df[stock_financial_analysis_indicator_df['日期'] == '2024-03-31'])
        stock_financial_analysis_indicator_df = stock_financial_analysis_indicator_df[
            stock_financial_analysis_indicator_df['日期'].astype(str).isin(['2024-03-31', '2023-12-31', '2022-12-31', '2021-12-31', '2020-12-31', '2019-12-31'])]

        output_file = f'fnc_{symbol}.xlsx'
        stock_financial_analysis_indicator_df.to_excel(
            output_file, index=False)

        stock_financial_analysis_indicator_df = stock_financial_analysis_indicator_df[
            stock_financial_analysis_indicator_df['营业利润率(%)'] > -0.1]

        if not stock_financial_analysis_indicator_df.empty:
            result.append(symbol)

    return result


# timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# output_file = f'kzz_{timestamp}.xlsx'
# stock_financial_analysis_indicator_df.to_excel(output_file, index=False)
# print(get_cash_data(["601611", "000876"]))
