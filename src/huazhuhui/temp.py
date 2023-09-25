# -*- coding: utf-8 -*-

def date_encrypt(date_str):
    # 声明一个密文字符串
    encrypted_text = ""

    # 创建一个字母表，包括数字和字母
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # 遍历日期字符串中的每个字符
    for char in date_str:
        # 计算字符在字母表中的位置
        index = int(char)

        # 将字母表中的字符添加到密文中
        encrypted_text += alphabet[index]

    return encrypted_text

# 用法示例
date = '0923'
encrypted_date = date_encrypt(date)
print("密文:", encrypted_date)
