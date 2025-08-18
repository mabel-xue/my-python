#!/bin/bash

# 飞书通知服务启动脚本（重构后版本）

# 设置工作目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/src/kezhuanzhai/scheduler"

# 检查Python环境
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装，请先安装Python3"
    exit 1
fi

# 检查依赖
echo "🔍 检查依赖..."
python3 -c "import requests, pandas, schedule, dotenv" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  缺少必要依赖，正在安装..."
    pip3 install requests pandas schedule python-dotenv
fi

# 检查配置文件
if [ ! -f "../../../.env" ]; then
    echo "⚠️  配置文件不存在，正在运行配置向导..."
    python3 setup_config.py
    if [ $? -ne 0 ]; then
        echo "❌ 配置失败，请手动配置"
        exit 1
    fi
fi

# 启动服务
echo "🚀 启动飞书通知服务..."
echo "📁 工作目录: $(pwd)"
echo "📝 日志文件: feishu_notifier.log"
echo "⏰ 执行时间: 每个工作日早上9:30"
echo "💡 按 Ctrl+C 停止服务"
echo ""

python3 feishu_notifier.py 