# 项目结构说明

## 飞书定时通知可转债监控系统

```
my-python/
├── src/
│   └── kezhuanzhai/
│       ├── feishu_notifier.py      # 主要功能文件：飞书通知和可转债监控
│       ├── config.py               # 配置文件
│       └── ...                     # 其他现有文件
├── setup_config.py                 # 配置向导脚本
├── test_notifier.py                # 功能测试脚本
├── start_notifier.sh               # Linux/macOS启动脚本
├── start_notifier.bat              # Windows启动脚本
├── README_feishu_notifier.md       # 详细使用说明
├── PROJECT_STRUCTURE.md            # 项目结构说明（本文件）
└── requirements.txt                 # Python依赖
```

## 文件功能说明

### 核心功能文件

1. **`feishu_notifier.py`** - 主要功能实现
   - `FeishuNotifier` 类：飞书消息发送
   - `ConvertibleBondMonitor` 类：可转债数据监控
   - 支持Webhook和API两种通知方式
   - 定时任务调度

2. **`config.py`** - 配置管理
   - 环境变量加载
   - 配置参数统一管理

### 配置和启动文件

3. **`setup_config.py`** - 配置向导
   - 交互式配置界面
   - 自动创建.env文件
   - 支持Webhook和应用凭证两种配置方式

4. **`start_notifier.sh`** - Linux/macOS启动脚本
   - 自动检查依赖
   - 自动配置检查
   - 一键启动服务

5. **`start_notifier.bat`** - Windows启动脚本
   - 功能同Linux版本
   - 适配Windows环境

### 测试和文档

6. **`test_notifier.py`** - 功能测试
   - 模块导入测试
   - 配置检查测试
   - 数据获取测试
   - 消息格式化测试
   - 飞书连接测试

7. **`README_feishu_notifier.md`** - 详细使用说明
   - 安装配置指南
   - 使用方法说明
   - 故障排除指南

## 使用流程

### 1. 首次使用
```bash
# 运行配置向导
python setup_config.py

# 测试功能
python test_notifier.py

# 启动服务
./start_notifier.sh  # Linux/macOS
# 或
start_notifier.bat   # Windows
```

### 2. 日常使用
```bash
# 直接启动
./start_notifier.sh

# 或后台运行
nohup ./start_notifier.sh > notifier.out 2>&1 &
```

### 3. 配置修改
```bash
# 重新运行配置向导
python setup_config.py

# 或直接编辑.env文件
vim .env
```

## 技术架构

### 数据流
```
集思录API → 数据获取 → 价格筛选 → 消息格式化 → 飞书发送
```

### 定时调度
```
schedule库 → 工作日9:30 → 执行监控任务
```

### 通知方式
```
Webhook方式（推荐）
├── 简单易用
├── 无需应用权限
└── 适合个人使用

API方式（高级）
├── 功能更强大
├── 可指定群聊
└── 适合企业使用
```

## 扩展性

### 可扩展的模块
1. **数据源**：支持其他可转债数据源
2. **筛选条件**：添加更多筛选条件
3. **通知方式**：支持其他IM平台
4. **数据存储**：数据库存储和查询
5. **Web界面**：管理界面和配置面板

### 配置项
- 价格阈值：`MAX_BOND_PRICE`
- 执行时间：`SCHEDULE_TIME`
- 通知方式：Webhook或API
- 群聊ID：`FEISHU_CHAT_ID`

## 注意事项

1. **依赖管理**：自动检查和安装Python依赖
2. **配置安全**：敏感信息存储在.env文件中
3. **日志记录**：详细的操作和错误日志
4. **错误处理**：完善的异常处理和重试机制
5. **跨平台**：支持Linux、macOS和Windows 