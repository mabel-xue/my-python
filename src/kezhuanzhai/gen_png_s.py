import pandas as pd

import matplotlib.pyplot as plt
from plottable import Table
import datetime
from matplotlib.font_manager import FontProperties

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# 读取 Excel 文件
df = pd.read_excel("已满足下修_20240713_220836.xlsx")

# 确保 Date 列为 datetime 类型
df["预估下修日"] = pd.to_datetime(df["预估下修日"])
df["到期时间"] = pd.to_datetime(df["到期时间"])

# 将 Date 列格式化为只包含日期的字符串
df["预估下修日"] = df["预估下修日"].dt.strftime("%Y-%m-%d")
df["到期时间"] = df["到期时间"].dt.strftime("%Y-%m-%d")

# 重命名索引列为 "序号" 并从 1 开始
df.index = df.index + 1
df.index.name = "序号"
# 使用 plottable 创建表格
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["savefig.bbox"] = "tight"
fig, ax = plt.subplots(figsize=(19, 19))
# 隐藏轴
ax.axis("tight")
ax.axis("off")
table = Table(
    df=df,
    row_dividers=False,
    odd_row_color="#FF929D",
    even_row_color="#FFCCD1",
    textprops={"fontsize": 12},
    column_border_kw={"linewidth": 1, "linestyle": "-"},
    col_label_cell_kw={
        "color": "white",
    },
)
# first_column_width = 0.1
# table.get_celld()[(0, 0)].set_width(first_column_width)
# for i in range(1, len(df.columns)):
#     table.get_celld()[(0, i)].set_width(0.15)

# 显示图表
plt.show()

# 保存图片
fig.savefig(f"table_{timestamp}.png", dpi=300)
