#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
飞书通知配置设置脚本
"""

import os
import sys
from pathlib import Path


def create_env_file():
    """创建.env配置文件"""
    # 获取项目根目录（向上3级到项目根目录）
    project_root = Path(__file__).parent.parent.parent.parent
    env_file = project_root / ".env"

    env_content = """# 飞书配置
# 方式1：使用Webhook（推荐，简单易用）
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/your_webhook_token_here

# 方式2：使用应用凭证（功能更强大，可以发送到指定群聊）
# FEISHU_APP_ID=your_app_id_here
# FEISHU_APP_SECRET=your_app_secret_here
# FEISHU_CHAT_ID=your_chat_id_here

# 可转债价格阈值（默认114）
MAX_BOND_PRICE=114.0

# 定时执行时间（默认每个工作日早上9:30）
SCHEDULE_TIME=09:30
"""
    if env_file.exists():
        print("⚠️  .env文件已存在，将覆盖现有配置")
        response = input("是否继续？(y/N): ")
        if response.lower() != "y":
            print("配置已取消")
            return False

    with open(env_file, "w", encoding="utf-8") as f:
        f.write(env_content)

    print("✅ .env配置文件已创建")
    return True


def setup_webhook():
    """设置Webhook配置"""
    print("\n🔧 设置飞书Webhook")
    print("1. 在飞书中创建一个机器人")
    print("2. 获取Webhook地址")
    print("3. 将地址填入下面的配置中")

    webhook_url = input("\n请输入Webhook地址: ").strip()

    if webhook_url and webhook_url.startswith("https://"):
        # 更新.env文件
        project_root = Path(__file__).parent.parent.parent.parent
        env_file = project_root / ".env"
        if env_file.exists():
            with open(env_file, "r", encoding="utf-8") as f:
                content = f.read()

            content = content.replace(
                "FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/your_webhook_token_here",
                f"FEISHU_WEBHOOK_URL={webhook_url}",
            )

            with open(env_file, "w", encoding="utf-8") as f:
                f.write(content)

            print("✅ Webhook配置已更新")
            return True
        else:
            print("❌ .env文件不存在，请先运行配置初始化")
            return False
    else:
        print("❌ Webhook地址格式不正确")
        return False


def setup_app_credentials():
    """设置应用凭证配置"""
    print("\n🔧 设置飞书应用凭证")
    print("1. 在飞书开放平台创建应用")
    print("2. 获取App ID和App Secret")
    print("3. 将信息填入下面的配置中")

    app_id = input("\n请输入App ID: ").strip()
    app_secret = input("请输入App Secret: ").strip()
    chat_id = input("请输入群聊ID（可选）: ").strip()

    if app_id and app_secret:
        # 更新.env文件
        project_root = Path(__file__).parent.parent.parent.parent
        env_file = project_root / ".env"
        if env_file.exists():
            with open(env_file, "r", encoding="utf-8") as f:
                content = f.read()

            # 注释掉Webhook配置
            content = content.replace("FEISHU_WEBHOOK_URL=", "# FEISHU_WEBHOOK_URL=")

            # 更新应用凭证配置
            content = content.replace(
                "# FEISHU_APP_ID=your_app_id_here", f"FEISHU_APP_ID={app_id}"
            )
            content = content.replace(
                "# FEISHU_APP_SECRET=your_app_secret_here",
                f"FEISHU_APP_SECRET={app_secret}",
            )

            if chat_id:
                content = content.replace(
                    "# FEISHU_CHAT_ID=your_chat_id_here", f"FEISHU_CHAT_ID={chat_id}"
                )

            with open(env_file, "w", encoding="utf-8") as f:
                f.write(content)

            print("✅ 应用凭证配置已更新")
            return True
        else:
            print("❌ .env文件不存在，请先运行配置初始化")
            return False
    else:
        print("❌ App ID和App Secret不能为空")
        return False


def setup_custom_config():
    """设置自定义配置"""
    print("\n🔧 设置自定义配置")

    max_price = input("请输入可转债价格阈值（默认114.0）: ").strip()
    schedule_time = input("请输入执行时间（默认09:30）: ").strip()

    if max_price or schedule_time:
        project_root = Path(__file__).parent.parent.parent.parent
        env_file = project_root / ".env"
        if env_file.exists():
            with open(env_file, "r", encoding="utf-8") as f:
                content = f.read()

            if max_price:
                try:
                    float(max_price)
                    content = content.replace(
                        "MAX_BOND_PRICE=114.0", f"MAX_BOND_PRICE={max_price}"
                    )
                    print("✅ 价格阈值已更新")
                except ValueError:
                    print("❌ 价格阈值格式不正确")

            if schedule_time:
                content = content.replace(
                    "SCHEDULE_TIME=09:30", f"SCHEDULE_TIME={schedule_time}"
                )
                print("✅ 执行时间已更新")

            with open(env_file, "w", encoding="utf-8") as f:
                f.write(content)

            return True
        else:
            print("❌ .env文件不存在，请先运行配置初始化")
            return False
    else:
        print("⚠️  未进行任何修改")
        return True


def test_configuration():
    """测试配置"""
    print("\n🧪 测试配置")

    # 检查.env文件
    project_root = Path(__file__).parent.parent.parent.parent
    env_file = project_root / ".env"
    if not env_file.exists():
        print("❌ .env文件不存在")
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
        print("\n✅ 配置完成！可以运行 feishu_notifier.py 了")
        return True
    else:
        print("\n❌ 配置不完整，请重新配置")
        return False


def main():
    """主函数"""
    print("🚀 飞书通知配置向导")
    print("=" * 50)

    while True:
        print("\n请选择操作：")
        print("1. 初始化配置文件")
        print("2. 设置Webhook")
        print("3. 设置应用凭证")
        print("4. 设置自定义配置")
        print("5. 测试配置")
        print("6. 退出")

        choice = input("\n请输入选择 (1-6): ").strip()

        if choice == "1":
            create_env_file()
        elif choice == "2":
            setup_webhook()
        elif choice == "3":
            setup_app_credentials()
        elif choice == "4":
            setup_custom_config()
        elif choice == "5":
            test_configuration()
        elif choice == "6":
            print("👋 再见！")
            break
        else:
            print("❌ 无效选择，请重新输入")


if __name__ == "__main__":
    main()
