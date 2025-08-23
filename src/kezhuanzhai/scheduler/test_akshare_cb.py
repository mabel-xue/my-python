#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试 akshare 可转债数据接口
"""

import akshare as ak
import pandas as pd


def test_cb_data():
    """测试可转债数据获取"""
    try:
        print("正在获取可转债数据...")

        # 尝试不同的接口
        print("1. 测试 bond_zh_cov (中证可转债):")
        try:
            cb_index = ak.bond_zh_cov()
            print(f"  数据形状: {cb_index.shape}")
            print(f"  列名: {list(cb_index.columns)}")
            print("  列名数量:", len(cb_index.columns))
            print("  前3行数据:")
            print(cb_index.head(3))
            print("\n  数据类型:")
            print(cb_index.dtypes)
            
            # 尝试打印所有列名
            print("\n  完整列名:")
            for i, col in enumerate(cb_index.columns, 1):
                print(f"{i}. {col}")
        except Exception as e:
            print(f"  接口1异常: {e}")
            import traceback
            traceback.print_exc()

        print("\n2. 测试 bond_cb_spot (可转债实时行情):")
        try:
            cb_spot = ak.bond_cb_spot()
            print(f"  数据形状: {cb_spot.shape}")
            print(f"  列名: {list(cb_spot.columns)}")
            if not cb_spot.empty:
                print("  前3行数据:")
                print(cb_spot.head(3))
        except Exception as e:
            print(f"  接口2异常: {e}")

        print("\n3. 测试 bond_cb_spot_em (东方财富可转债实时行情):")
        try:
            cb_spot_em = ak.bond_cb_spot_em()
            print(f"  数据形状: {cb_spot_em.shape}")
            print(f"  列名: {list(cb_spot_em.columns)}")
            if not cb_spot_em.empty:
                print("  前3行数据:")
                print(cb_spot_em.head(3))
        except Exception as e:
            print(f"  接口3异常: {e}")

        return True

    except Exception as e:
        print(f"测试异常: {e}")
        return False


if __name__ == "__main__":
    test_cb_data()
