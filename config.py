#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置文件
"""

import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 飞书配置
FEISHU_CONFIG = {
    # 方式1：使用Webhook（推荐，简单易用）
    "webhook_url": os.getenv("FEISHU_WEBHOOK_URL"),
    # 方式2：使用应用凭证（功能更强大，可以发送到指定群聊）
    "app_id": os.getenv("FEISHU_APP_ID"),
    "app_secret": os.getenv("FEISHU_APP_SECRET"),
    "chat_id": os.getenv("FEISHU_CHAT_ID"),
}

# 可转债配置
BOND_CONFIG = {
    "max_price": float(os.getenv("MAX_BOND_PRICE", "114.0")),  # 价格阈值
    "schedule_time": os.getenv("SCHEDULE_TIME", "09:30"),  # 定时执行时间
}

# 数据源配置
DATA_SOURCE_CONFIG = {
    "jisilu_url": "https://app.jisilu.cn/data/cbnew/cb_list/",
    "timeout": 15,
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

# 日志配置
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(levelname)s - %(message)s",
    "file": "feishu_notifier.log",
    "encoding": "utf-8",
}
