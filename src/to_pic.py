# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import json

# 读取 JSON 文件
with open('./data.json') as f:
    data = json.load(f)

# 创建图片并绘制文本
img = Image.new('RGB', (800, 600), color = (255, 255, 255))
d = ImageDraw.Draw(img)
font = ImageFont.truetype('Arial Unicode.ttf', 16)
x, y = 50, 50
for item in data:
    for i in item:
      # print(i)
    # text = item['title'] + ': ' + item['description']
      d.text((x, y), i, fill=(0, 0, 0), font=font)
      y += 20

# 保存图片
img.save('output.png')
