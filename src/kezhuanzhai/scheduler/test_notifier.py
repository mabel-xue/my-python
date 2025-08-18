#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
飞书通知功能测试脚本
"""

import sys
import os
from pathlib import Path
from datetime import datetime

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root / "src" / "kezhuanzhai" / "scheduler"))


def test_imports():
    """测试模块导入"""
    print("🧪 测试模块导入...")

    try:
        from feishu_notifier import FeishuNotifier, ConvertibleBondMonitor

        print("✅ 模块导入成功")
        return True
    except ImportError as e:
        print(f"❌ 模块导入失败: {e}")
        return False


def test_config():
    """测试配置"""
    print("\n🔧 测试配置...")

    # 检查.env文件
    env_file = project_root / ".env"
    if not env_file.exists():
        print("❌ .env配置文件不存在")
        print("请先运行 setup_config.py 进行配置")
        return False

    # 加载环境变量
    from dotenv import load_dotenv

    load_dotenv()

    webhook_url = os.getenv("FEISHU_WEBHOOK_URL")
    app_id = os.getenv("FEISHU_APP_ID")
    app_secret = os.getenv("FEISHU_APP_SECRET")

    print(f"Webhook URL: {'✅ 已配置' if webhook_url else '❌ 未配置'}")
    print(f"App ID: {'✅ 已配置' if app_id else '❌ 未配置'}")
    print(f"App Secret: {'✅ 已配置' if app_secret else '❌ 未配置'}")

    if webhook_url or (app_id and app_secret):
        print("✅ 配置检查通过")
        return True
    else:
        print("❌ 配置不完整")
        return False


def test_data_fetch():
    """测试数据获取"""
    print("\n📊 测试数据获取...")

    try:
        from feishu_notifier import ConvertibleBondMonitor

        monitor = ConvertibleBondMonitor()

        # 获取可转债数据
        bonds_data = monitor.get_convertible_bonds_data()
        if bonds_data:
            print(f"✅ 成功获取 {len(bonds_data)} 条可转债数据")

            # 筛选低价可转债
            low_price_bonds = monitor.filter_low_price_bonds(bonds_data)
            print(f"✅ 发现 {len(low_price_bonds)} 只价格低于114的可转债")

            if low_price_bonds:
                print("\n📋 低价可转债列表:")
                for i, bond in enumerate(low_price_bonds[:3], 1):  # 只显示前3只
                    print(
                        f"  {i}. {bond['代码']} {bond['转债名']} - 价格: {bond['价格']}"
                    )

            return True
        else:
            print("❌ 未获取到可转债数据")
            return False

    except Exception as e:
        print(f"❌ 数据获取测试失败: {e}")
        return False


def test_message_format():
    """测试消息格式化"""
    print("\n💬 测试消息格式化...")

    try:
        from feishu_notifier import ConvertibleBondMonitor

        monitor = ConvertibleBondMonitor()

        # 模拟数据
        mock_bonds = [
            {
                "代码": "113542",
                "转债名": "华海转债",
                "价格": 112.50,
                "溢价率": "15.2%",
                "转股价": "25.60",
                "正股价": "24.80",
                "申购日期": "2024-01-15",
                "申购代码": "733542",
                "申购上限": "100",
                "正股代码": "600521",
                "转股价值": "96.88",
                "发行规模": "18.00",
                "中签率": "0.0123",
                "上市时间": "2024-01-25",
                "信用评级": "AA+",
            }
        ]

        message = monitor.format_message(mock_bonds)
        print("✅ 消息格式化成功")
        print("\n📝 消息预览:")
        print("-" * 50)
        print(message[:200] + "..." if len(message) > 200 else message)
        print("-" * 50)

        return True

    except Exception as e:
        print(f"❌ 消息格式化测试失败: {e}")
        return False


def test_feishu_connection():
    """测试飞书连接并发送实际消息"""
    print("\n🔗 测试飞书连接并发送消息...")

    try:
        from feishu_notifier import FeishuNotifier

        # 创建通知器实例
        notifier = FeishuNotifier()
        print("✅ 飞书通知器创建成功")

        # 检查配置
        if notifier.webhook_url:
            print("✅ Webhook配置正常")
        elif notifier.access_token:
            print("✅ API配置正常")
        else:
            print("❌ 飞书配置异常")
            return False

        # 发送测试消息
        test_message = "🧪 这是一条测试消息\n\n📅 发送时间: " + datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        test_message += "\n\n✅ 飞书通知功能测试成功！"

        print("📤 正在发送测试消息...")
        success = notifier.send_message(test_message)

        if success:
            print("✅ 测试消息发送成功！")
            print("📱 请检查飞书群或私聊消息")
        else:
            print("❌ 测试消息发送失败")
            return False

        return True

    except Exception as e:
        print(f"❌ 飞书连接测试失败: {e}")
        return False


def main():
    """主测试函数"""
    print("🚀 飞书通知功能测试")
    print("=" * 50)

    tests = [
        ("模块导入", test_imports),
        ("配置检查", test_config),
        ("数据获取", test_data_fetch),
        ("消息格式化", test_message_format),
        ("飞书连接", test_feishu_connection),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                print(f"⚠️  {test_name} 测试失败")
        except Exception as e:
            print(f"❌ {test_name} 测试异常: {e}")

    print("\n" + "=" * 50)
    print(f"📊 测试结果: {passed}/{total} 通过")

    if passed == total:
        print("🎉 所有测试通过！可以正常运行飞书通知服务")
        print("\n💡 运行以下命令启动服务:")
        print("  Linux/macOS: ./start_notifier.sh")
        print("  Windows: start_notifier.bat")
        print("  或直接运行: python src/kezhuanzhai/feishu_notifier.py")
    else:
        print("⚠️  部分测试失败，请检查配置和依赖")
        print("\n🔧 运行以下命令进行配置:")
        print("  python setup_config.py")


if __name__ == "__main__":
    main()
