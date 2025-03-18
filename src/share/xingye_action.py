import akshare as ak
from datetime import datetime, timedelta

# 获取今天的日期，格式为 "YYYYMMDD"
today = datetime.today().strftime("%Y%m%d")
# 获取 40 天前的日期，格式为 "YYYYMMDD"
start_date = (datetime.today() - timedelta(days=40)).strftime("%Y%m%d")

stock_zh_a_daily_qfq_df = ak.stock_zh_a_daily(
    symbol="sh601166", start_date=start_date, end_date=today, adjust="qfq"
)
# print(stock_zh_a_daily_qfq_df)

# 确保数据中包含成交量信息
if "volume" in stock_zh_a_daily_qfq_df.columns:
    total_rows = len(stock_zh_a_daily_qfq_df)
    # 取最近 40 天的数据
    stock_zh_a_daily_qfq_df = stock_zh_a_daily_qfq_df.tail(total_rows)

    # 计算前 20 天和近 20 天的成交量总和
    half_rows = total_rows // 2  # 总条数的一半
    previous_20_days_volume = stock_zh_a_daily_qfq_df["volume"].iloc[:half_rows].sum()
    # print(f"前 20 天的成交量: {previous_20_days_volume}")
    recent_20_days_volume = stock_zh_a_daily_qfq_df["volume"].iloc[half_rows:].sum()
    # print(f"近 20 天的成交量: {recent_20_days_volume}")

    # 计算环比变化
    if previous_20_days_volume != 0:
        volume_change_ratio = (
            (recent_20_days_volume - previous_20_days_volume) / previous_20_days_volume
        ) * 100
        print(f"近 20 天的成交量环比变化: {volume_change_ratio:.2f}%")
    else:
        print("前 20 天的成交量为 0，无法计算环比变化")
else:
    print("数据中不包含成交量信息")


def calcMean(original_df):
    stock_zh_a_daily_qfq_df = original_df.copy()

    # 确保数据中包含必要的列
    if {"high", "low", "close"}.issubset(stock_zh_a_daily_qfq_df.columns):
        # 计算最高涨幅和最低涨幅
        stock_zh_a_daily_qfq_df["前一天收盘价"] = stock_zh_a_daily_qfq_df[
            "close"
        ].shift(1)
        stock_zh_a_daily_qfq_df["最高涨幅"] = (
            (stock_zh_a_daily_qfq_df["high"] - stock_zh_a_daily_qfq_df["前一天收盘价"])
            / stock_zh_a_daily_qfq_df["前一天收盘价"]
        ) * 100
        stock_zh_a_daily_qfq_df["最低涨幅"] = (
            (stock_zh_a_daily_qfq_df["low"] - stock_zh_a_daily_qfq_df["前一天收盘价"])
            / stock_zh_a_daily_qfq_df["前一天收盘价"]
        ) * 100

        # 打印结果
        # print(stock_zh_a_daily_qfq_df[["high", "low", "close", "最高涨幅", "最低涨幅"]])
        # 计算最高涨幅和最低涨幅的均值
        mean_high = stock_zh_a_daily_qfq_df["最高涨幅"].mean()
        mean_low = stock_zh_a_daily_qfq_df["最低涨幅"].mean()

        # 获取最新收盘价
        latest_close_price = stock_zh_a_daily_qfq_df["close"].iloc[-1]

        # 计算委托买价
        buy_price = latest_close_price * (1 + mean_low / 100)

        # 打印结果
        print(f"最高涨幅均值: {mean_high:.2f}%")
        print(f"最低涨幅均值: {mean_low:.2f}%")
        print(f"委托买价: {buy_price:.2f}")
    else:
        print("数据中不包含必要的列：high, low, close")


print("前 20 天")
calcMean(stock_zh_a_daily_qfq_df.head(half_rows))
print("近 20 天")
calcMean(stock_zh_a_daily_qfq_df.tail(half_rows))
today_close_price = stock_zh_a_daily_qfq_df.tail(1)["close"].iloc[0]
print(f"当日收盘价: {today_close_price:.2f}")
buy_price = today_close_price * (1 + 0.36 / 100)
print(f"+0.36%: {buy_price:.2f}")
buy_price = today_close_price * (1 - 0.36 / 100)
print(f"-0.36%: {buy_price:.2f}")
