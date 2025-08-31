#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
根据可转债名称查询功能
"""

import os
import sys
import yaml
from dotenv import load_dotenv
from feishu_notifier import ConvertibleBondMonitor

# 加载环境变量
load_dotenv()


def load_config(config_path="config.yaml"):
    """从配置文件加载配置"""
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def test_query_bonds():
    """测试查询可转债功能"""
    print("=== 测试根据可转债名称查询功能 ===\n")

    try:
        monitor = ConvertibleBondMonitor()

        # 从配置文件读取测试用例
        config = load_config()
        test_bond_names = config.get("test_bond_names", [])

        print(f"正在查询可转债: {', '.join(test_bond_names)}")

        # 查询可转债信息
        bonds_info = monitor.query_bonds_by_names(test_bond_names)

        if bonds_info:
            print(f"\n成功查询到 {len(bonds_info)} 只可转债信息：\n")

            for i, bond in enumerate(bonds_info, 1):
                print(f"{i}. {bond.get('代码', '')} {bond.get('转债名', '')}")
                print(f"   行业: {bond.get('行业', '')}")
                print(f"   现价: {bond.get('现价', 0):.2f}")
                print(f"   转债流通市值占比: {bond.get('转债流通市值占比', '')}")
                print(f"   正股PB: {bond.get('正股PB', '')}")
                print(f"   到期时间: {bond.get('到期时间', '')}")
                print(f"   信用评级: {bond.get('信用评级', '')}")
                print(
                    f"   正股: {bond.get('正股代码', '')} {bond.get('正股简称', '')} ({bond.get('正股价', '')})"
                )
                print(
                    f"   转股价: {bond.get('转股价', '')} | 溢价率: {bond.get('溢价率', '')}%"
                )
                print()
        else:
            print("未找到匹配的可转债信息")

    except Exception as e:
        print(f"测试过程中发生异常: {e}")
        import traceback

        traceback.print_exc()


def test_query_and_notify():
    """测试查询并发送飞书通知功能"""
    print("=== 测试查询并发送飞书通知功能 ===\n")

    try:
        monitor = ConvertibleBondMonitor()

        # 从配置文件读取测试用例
        config = load_config()
        test_bond_names = config.get("test_bond_names", [])

        print(f"正在查询并发送通知: {', '.join(test_bond_names)}")

        # 查询并发送通知
        monitor.query_and_notify_bonds(test_bond_names)

        print("测试完成")

    except Exception as e:
        print(f"测试过程中发生异常: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    # 检查是否配置了飞书
    if not os.getenv("FEISHU_WEBHOOK_URL") and not (
        os.getenv("FEISHU_APP_ID") and os.getenv("FEISHU_APP_SECRET")
    ):
        print("警告: 未配置飞书webhook或应用信息，将跳过通知测试")
        print("只测试查询功能...")
        test_query_bonds()
    else:
        print("检测到飞书配置，运行完整测试...")
        # test_query_bonds()
        print("\n" + "=" * 50 + "\n")
        test_query_and_notify()
