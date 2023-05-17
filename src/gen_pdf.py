# -*- coding: utf-8 -*-
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

# 图像文件列表
image_files = [
    'image1.gif',
    'image2.gif',
    'image3.gif',
    'image4.gif',
    'image5.gif',
    'image6.gif',
    'image7.gif',
    'image8.gif',
    'image9.gif',
    'image10.gif',
    'image11.gif',
    'image12.gif',
    'image13.gif',
    'image14.gif',
    'image15.gif',
    ]

# 创建一个PDF文件
c = canvas.Canvas('images.pdf', pagesize=letter)

# 遍历所有图像并将其添加到PDF文件中
for i, image_file in enumerate(image_files):
    # 打开图像文件
    im = Image.open(image_file)
    
    # 获取图像的宽度和高度
    width, height = im.size
    
    # 计算图像的宽度和高度适合在PDF中的大小
    aspect = height / float(width)
    new_height = aspect * letter[0]
    
    # 将图像添加到PDF文件中
    c.drawImage(image_file, 0, 0, letter[0]-10, new_height-15)
    
    # 如果不是最后一张图像，则添加一个新的页面
    if i < len(image_files) - 1:
        c.showPage()

# 保存PDF文件
c.save()
