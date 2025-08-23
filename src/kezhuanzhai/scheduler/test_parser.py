#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试可转债HTML解析功能
"""

from feishu_notifier import ConvertibleBondMonitor
import json

def test_parse_detail():
    """测试解析可转债详情页功能"""
    monitor = ConvertibleBondMonitor()
    
    # 读取示例HTML文件
    with open('kezhuanzhan.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 解析HTML内容
    result = monitor.parse_convertible_bond_detail(html_content, '110092')
    
    # 打印解析结果
    print("=== 可转债详情解析结果 ===")
    print(f"债券代码: {result['bond_code']}")
    print(f"行业: {result['industry']}")
    print(f"地域: {result['region']}")
    print(f"相关公告数量: {len(result['announcements'])}")
    print("\n前5个公告:")
    for i, announcement in enumerate(result['announcements'][:5]):
        print(f"{i+1}. {announcement['title']}")
        print(f"   日期: {announcement['date']}")
        print(f"   链接: {announcement['url']}")
        print()
    
    # 保存结果到JSON文件
    with open('test_result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"解析结果已保存到 test_result.json")

def test_get_detail():
    """测试获取可转债详情页功能"""
    monitor = ConvertibleBondMonitor()
    
    # 测试获取三房转债详情
    result = monitor.get_convertible_bond_detail('110092')
    
    print("=== 在线获取可转债详情结果 ===")
    print(f"债券代码: {result['bond_code']}")
    print(f"行业: {result['industry']}")
    print(f"地域: {result['region']}")
    print(f"相关公告数量: {len(result['announcements'])}")

if __name__ == "__main__":
    print("测试1: 解析本地HTML文件")
    test_parse_detail()
    
    print("\n" + "="*50 + "\n")
    
    print("测试2: 在线获取并解析")
    test_get_detail()