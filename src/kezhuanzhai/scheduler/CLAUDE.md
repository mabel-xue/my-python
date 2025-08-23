# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **convertible bond (可转债) monitoring and notification system** that tracks low-priced convertible bonds in the Chinese A-share market and sends alerts via Feishu (Lark).

### Core Architecture

The system consists of two main classes:

1. **`FeishuNotifier`** (feishu_notifier.py:35-138): Handles Feishu message delivery via webhook or API
2. **`ConvertibleBondMonitor`** (feishu_notifier.py:140-646): Manages bond data fetching, filtering, and monitoring logic

### Key Features

- **Data Source**: Uses `akshare` library to fetch real-time convertible bond data
- **Filtering Logic**: Monitors bonds with price < 114 RMB, valid credit ratings (AAA to A), stock price > 1 RMB
- **Watch Pool**: Special monitoring list for specific bond codes (configurable via environment variable)
- **Rich Notifications**: Sends both plain text and interactive card messages to Feishu
- **Scheduled Execution**: Runs automatically on weekdays at 9:30 AM

## Development Commands

### Running the Application

```bash
# Run the main monitor (with immediate check + scheduled execution)
python feishu_notifier.py

# Run configuration setup wizard
python setup_config.py

# Test specific functionality
python test.py                    # Test akshare integration
python test_notifier.py          # Test notification system
python test_parser.py            # Test HTML parsing
python test_format.py            # Test message formatting
python test_watch_pool.py        # Test watch pool functionality
```

### Environment Configuration

The application requires a `.env` file in the project root with:

```bash
# Feishu webhook (method 1 - recommended)
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/your_token

# OR Feishu app credentials (method 2)
FEISHU_APP_ID=your_app_id
FEISHU_APP_SECRET=your_app_secret
FEISHU_CHAT_ID=your_chat_id

# Optional configurations
WATCH_BOND_CODES=110092,113025,128136  # Comma-separated bond codes
MAX_BOND_PRICE=114.0
SCHEDULE_TIME=09:30
```

Use `python setup_config.py` for interactive configuration setup.

### Dependencies

Core dependencies (install manually if needed):
- `akshare`: Chinese financial data API
- `requests`: HTTP requests
- `pandas`: Data manipulation
- `schedule`: Task scheduling
- `beautifulsoup4`: HTML parsing
- `python-dotenv`: Environment variable management

## Code Architecture Details

### Data Flow

1. **Data Acquisition** (feishu_notifier.py:165-320): `get_convertible_bonds_data()` fetches data via akshare
2. **Filtering** (feishu_notifier.py:434-492): `filter_low_price_bonds()` applies business rules
3. **Enhancement** (feishu_notifier.py:402-432): `get_convertible_bond_detail()` scrapes additional data from jisilu.cn
4. **Formatting** (feishu_notifier.py:494-612): `format_message()` creates text and card content
5. **Notification** (feishu_notifier.py:614-646): `check_and_notify()` orchestrates the pipeline

### Configuration System

- Environment variables loaded via `python-dotenv`
- `setup_config.py` provides interactive configuration wizard
- Supports both webhook and OAuth2 authentication methods for Feishu

### Testing Structure

Each test file focuses on a specific component:
- `test_akshare_cb.py`: Data source integration
- `test_notifier.py`: Message delivery
- `test_parser.py`: HTML parsing logic
- `test_format.py`: Message formatting
- `test_watch_pool.py`: Special monitoring features

### Watch Pool System

Special monitoring for specific bonds configured via `WATCH_BOND_CODES` environment variable. Watched bonds are highlighted with "🚨 (监控中)" in notifications and appear in bold in text messages.

## Important Notes

- **Market Hours**: Scheduled for weekday mornings (9:30 AM) when Chinese markets open
- **Rate Limiting**: Built-in delays and error handling for external API calls
- **Data Quality**: Filters out invalid data (NaN prices, unrated bonds, delisted stocks)
- **Logging**: Comprehensive logging to `feishu_notifier.log` and console
- **Error Handling**: Graceful degradation when external services are unavailable