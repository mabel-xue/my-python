#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试修改后的format_message方法
"""

from feishu_notifier import ConvertibleBondMonitor

def test_format_message_with_detail():
    """测试包含详情信息的消息格式化"""
    monitor = ConvertibleBondMonitor()
    
    # 模拟一个低价可转债数据
    test_bonds = [
        {
            '代码': '110092',
            '转债名': '三房转债',
            '价格': 103.10,
            '溢价率': '58.86',
            '转股价': '3.02',
            '正股价': '1.96',
            '正股代码': '600370',
            '正股简称': '三房巷',
            '发行规模': 25.0,
            '上市时间': '2023-02-07',
            '信用评级': 'A+'
        }
    ]
    
    # 格式化消息
    message = monitor.format_message(test_bonds)
    
    print("=== 测试消息格式 ===")
    print(message)
    print("=== 测试完成 ===")

if __name__ == "__main__":
    test_format_message_with_detail()