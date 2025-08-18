# 飞书定时通知可转债监控系统

## 功能描述

这是一个自动监控A股可转债价格的系统，当发现价格低于114的可转债时，会自动发送飞书消息通知。

## 主要特性

- 🔔 自动监控可转债价格
- 📊 筛选价格低于114的可转债
- ⏰ 每个工作日定时执行（默认早上9:30）
- 📱 支持飞书Webhook和API两种通知方式
- 📝 详细的日志记录
- 🎯 可配置的价格阈值和执行时间

## 安装依赖

```bash
pip install requests pandas schedule python-dotenv
```

## 配置说明

### 方式1：使用Webhook（推荐，简单易用）

1. 在飞书中创建一个机器人，获取Webhook地址
2. 设置环境变量：

```bash
export FEISHU_WEBHOOK_URL="https://open.feishu.cn/open-apis/bot/v2/hook/your_webhook_token_here"
```

### 方式2：使用应用凭证（功能更强大）

1. 在飞书开放平台创建应用
2. 获取App ID和App Secret
3. 设置环境变量：

```bash
export FEISHU_APP_ID="your_app_id_here"
export FEISHU_APP_SECRET="your_app_secret_here"
export FEISHU_CHAT_ID="your_chat_id_here"  # 可选，指定群聊ID
```

### 其他配置

```bash
export MAX_BOND_PRICE="114.0"        # 价格阈值
export SCHEDULE_TIME="09:30"         # 执行时间
```

## 使用方法

### 1. 直接运行

```bash
cd src/kezhuanzhai
python feishu_notifier.py
```

### 2. 后台运行

```bash
nohup python feishu_notifier.py > feishu_notifier.out 2>&1 &
```

### 3. 使用系统服务（Linux/macOS）

创建服务文件 `/etc/systemd/system/feishu-notifier.service`：

```ini
[Unit]
Description=Feishu Convertible Bond Notifier
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/your/project/src/kezhuanzhai
ExecStart=/path/to/your/python /path/to/your/project/src/kezhuanzhai/feishu_notifier.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

启动服务：

```bash
sudo systemctl daemon-reload
sudo systemctl enable feishu-notifier
sudo systemctl start feishu-notifier
```

## 消息格式示例

```
🔔 A股可转债价格监控通知 (2024-01-15 09:30:00)

📊 发现 5 只价格低于114的可转债：

1. 113542 华海转债
   价格: 112.50 | 溢价率: 15.2%
   到期收益率: 2.8% | 剩余年限: 2.5年
   转股价: 25.60 | 正股价: 24.80
   PB: 1.2 | ROE: 12.5%

2. 127041 华海转债
   价格: 113.20 | 溢价率: 18.5%
   到期收益率: 3.1% | 剩余年限: 3.2年
   转股价: 26.80 | 正股价: 25.90
   PB: 1.1 | ROE: 11.8%

💡 投资有风险，入市需谨慎！
```

## 日志文件

程序运行时会生成 `feishu_notifier.log` 日志文件，记录所有操作和错误信息。

## 注意事项

1. **数据源**：使用集思录的公开API获取可转债数据
2. **执行时间**：默认每个工作日早上9:30执行，避开股市开盘时间
3. **网络要求**：需要能够访问集思录和飞书API
4. **频率限制**：飞书API有调用频率限制，建议不要过于频繁
5. **数据准确性**：数据来源于第三方，仅供参考，投资决策请谨慎

## 故障排除

### 常见问题

1. **无法获取可转债数据**
   - 检查网络连接
   - 确认集思录API是否正常

2. **飞书消息发送失败**
   - 检查Webhook地址或应用凭证是否正确
   - 确认飞书应用权限设置

3. **定时任务不执行**
   - 检查系统时间是否正确
   - 确认程序是否在后台正常运行

### 调试模式

修改日志级别为DEBUG：

```python
logging.basicConfig(level=logging.DEBUG)
```

## 扩展功能

可以根据需要修改以下部分：

1. **数据源**：支持其他可转债数据源
2. **筛选条件**：添加更多筛选条件（如溢价率、到期收益率等）
3. **通知方式**：支持钉钉、企业微信等其他通知方式
4. **数据存储**：将数据保存到数据库或文件
5. **Web界面**：添加Web管理界面

## 许可证

本项目仅供学习和研究使用，请勿用于商业用途。 