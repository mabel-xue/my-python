import akshare as ak
import pandas as pd
# from datetime import datetime1


def get_cash_data(stock_symbols):
    result_df = pd.DataFrame()
    for symbol in stock_symbols:
        stock_xjll_em = ak.stock_financial_cash_ths(
            symbol=symbol, indicator="按报告期")

        stock_xjll_em = stock_xjll_em[
            stock_xjll_em['报告期'].astype(str) == "2024-03-31"]

        output_file = f'cash_{symbol}.xlsx'
        stock_xjll_em.to_excel(
            output_file, index=False)

        stock_xjll_em["正股代码"] = symbol
        stock_xjll_em['期末现金及现金等价物余额'] = stock_xjll_em['*期末现金及现金等价物余额'].str.replace(
            '亿', '')
        selected_columns = ["正股代码", "期末现金及现金等价物余额"]
        stock_xjll_em = stock_xjll_em.loc[:, selected_columns]
        print('== get_cash_data ==', symbol)
        result_df = pd.concat([result_df, stock_xjll_em])

    # print('== get_cash_data::result_df ==', result_df)
    return result_df


# timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# output_file = f'kzz_{timestamp}.xlsx'
# stock_xjll_em.to_excel(output_file, index=False)
# print(get_stock_xjll_em_data(["601611", "000876"]))
