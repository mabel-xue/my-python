#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
飞书定时通知可转债低于114的列表信息
"""

import requests
import json
import pandas as pd
import schedule
import time
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any
import os
from dotenv import load_dotenv
import akshare as ak
from bs4 import BeautifulSoup

# 加载环境变量
load_dotenv()

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("feishu_notifier.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


class FeishuNotifier:
    """飞书消息通知器"""

    def __init__(self):
        # 从环境变量获取飞书配置
        self.webhook_url = os.getenv("FEISHU_WEBHOOK_URL")
        self.app_id = os.getenv("FEISHU_APP_ID")
        self.app_secret = os.getenv("FEISHU_APP_SECRET")

        if not self.webhook_url and not (self.app_id and self.app_secret):
            raise ValueError("请配置飞书webhook_url或app_id和app_secret")

        self.access_token = None
        if self.app_id and self.app_secret:
            self.access_token = self._get_access_token()

    def _get_access_token(self) -> str:
        """获取飞书访问令牌"""
        try:
            url = (
                "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
            )
            data = {"app_id": self.app_id, "app_secret": self.app_secret}
            response = requests.post(url, json=data, timeout=10)
            response.raise_for_status()
            result = response.json()

            if result.get("code") == 0:
                return result.get("tenant_access_token")
            else:
                logger.error(f"获取飞书访问令牌失败: {result}")
                return None
        except Exception as e:
            logger.error(f"获取飞书访问令牌异常: {e}")
            return None

    def send_webhook_message(self, content: str) -> bool:
        """通过webhook发送消息"""
        try:
            data = {"msg_type": "text", "content": {"text": content}}
            response = requests.post(self.webhook_url, json=data, timeout=10)
            response.raise_for_status()
            result = response.json()

            if result.get("code") == 0:
                logger.info("webhook消息发送成功")
                return True
            else:
                logger.error(f"webhook消息发送失败: {result}")
                return False
        except Exception as e:
            logger.error(f"webhook消息发送异常: {e}")
            return False

    def send_api_message(self, chat_id: str, content: str) -> bool:
        """通过API发送消息"""
        if not self.access_token:
            logger.error("访问令牌无效")
            return False

        try:
            url = "https://open.feishu.cn/open-apis/im/v1/messages"
            headers = {
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json",
            }
            data = {
                "receive_id": chat_id,
                "msg_type": "text",
                "content": json.dumps({"text": content}),
            }
            response = requests.post(url, json=data, headers=headers, timeout=10)
            response.raise_for_status()
            result = response.json()

            if result.get("code") == 0:
                logger.info("API消息发送成功")
                return True
            else:
                logger.error(f"API消息发送失败: {result}")
                return False
        except Exception as e:
            logger.error(f"API消息发送异常: {e}")
            return False

    def send_message(self, content: str, chat_id: str = None) -> bool:
        """发送消息"""
        if self.webhook_url:
            return self.send_webhook_message(content)
        elif chat_id and self.access_token:
            return self.send_api_message(chat_id, content)
        else:
            logger.error("无法发送消息：缺少必要的配置")
            return False


class ConvertibleBondMonitor:
    """可转债监控器"""

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        self.feishu = FeishuNotifier()

    def get_convertible_bonds_data(self) -> List[Dict[str, Any]]:
        """获取可转债数据"""
        try:
            # 使用 akshare 库获取可转债数据
            logger.info("正在使用 akshare 获取可转债数据...")

            # 获取可转债基本信息
            cb_data = ak.bond_zh_cov()

            if cb_data.empty:
                logger.error("未获取到可转债数据")
                return []

            # 打印列名以便调试
            logger.info(f"akshare 返回的列名: {list(cb_data.columns)}")

            # 定义预期的列名，按照重要性排序
            expected_columns = [
                "债券代码",
                "债券简称",
                "申购日期",
                "申购代码",
                "申购上限",
                "正股代码",
                "正股简称",
                "正股价",
                "转股价",
                "转股价值",
                "债现价",
                "转股溢价率",
                "发行规模",
                "中签率",
                "上市时间",
                "信用评级",
            ]

            # 检查列名是否匹配
            missing_columns = [
                col for col in expected_columns if col not in cb_data.columns
            ]
            if missing_columns:
                logger.warning(f"缺少以下列: {missing_columns}")

            # 选择实际存在的列
            available_columns = [
                col for col in expected_columns if col in cb_data.columns
            ]

            # 转换为字典列表格式，保持与原代码兼容
            bonds_list = []
            for _, row in cb_data.iterrows():
                try:
                    # 安全获取数据，处理可能的 NaN 值
                    price = row.get("债现价", 0)
                    if pd.isna(price):
                        price = 0

                    # 动态构建 bond_info，只使用可用的列
                    bond_info = {
                        "cell": {
                            "bond_id": (
                                str(row.get("债券代码", "")).strip()
                                if "债券代码" in available_columns
                                else ""
                            ),
                            "bond_nm": (
                                str(row.get("债券简称", "")).strip()
                                if "债券简称" in available_columns
                                else ""
                            ),
                            "price": float(price),
                            "premium_rt": (
                                str(row.get("转股溢价率", "")).strip()
                                if "转股溢价率" in available_columns
                                else ""
                            ),
                            "ytm_rt": "N/A",  # 新接口暂无到期收益率
                            "year_left": "N/A",  # 新接口暂无剩余年限
                            "convert_price": (
                                str(row.get("转股价", "")).strip()
                                if "转股价" in available_columns
                                else ""
                            ),
                            "stock_price": (
                                str(row.get("正股价", "")).strip()
                                if "正股价" in available_columns
                                else ""
                            ),
                            "pb": "N/A",  # 新接口暂无PB
                            "roe": "N/A",  # 新接口暂无ROE
                            "申购日期": (
                                str(row.get("申购日期", "")).strip()
                                if "申购日期" in available_columns
                                else ""
                            ),
                            "申购代码": (
                                str(row.get("申购代码", "")).strip()
                                if "申购代码" in available_columns
                                else ""
                            ),
                            "申购上限": (
                                row.get("申购上限", 0)
                                if "申购上限" in available_columns
                                else 0
                            ),
                            "正股代码": (
                                str(row.get("正股代码", "")).strip()
                                if "正股代码" in available_columns
                                else ""
                            ),
                            "正股简称": (
                                str(row.get("正股简称", "")).strip()
                                if "正股简称" in available_columns
                                else ""
                            ),
                            "转股价值": (
                                str(row.get("转股价值", "")).strip()
                                if "转股价值" in available_columns
                                else ""
                            ),
                            "发行规模": (
                                row.get("发行规模", 0)
                                if "发行规模" in available_columns
                                else 0
                            ),
                            "中签率": (
                                row.get("中签率", 0)
                                if "中签率" in available_columns
                                else 0
                            ),
                            "上市时间": (
                                str(row.get("上市时间", "")).strip()
                                if "上市时间" in available_columns
                                else ""
                            ),
                            "信用评级": (
                                str(row.get("信用评级", "")).strip()
                                if "信用评级" in available_columns
                                else ""
                            ),
                        }
                    }
                    bonds_list.append(bond_info)
                except Exception as e:
                    logger.warning(f"处理单只可转债数据异常: {e}, 数据: {row}")
                    continue

            logger.info(f"成功获取 {len(bonds_list)} 只可转债数据")
            return bonds_list

        except Exception as e:
            logger.error(f"获取可转债数据异常: {e}")
            # 如果是列数不匹配的错误，尝试打印更多调试信息
            if "Length mismatch" in str(e):
                logger.error("可能是列数不匹配导致的错误，请检查数据源")
            return []

    def parse_convertible_bond_detail(
        self, html_content: str, bond_code: str
    ) -> Dict[str, Any]:
        """
        解析可转债详情页HTML源代码，提取行业、地域、到期日、转债流通市值占比、相关公告信息

        Args:
            html_content: 从 https://www.jisilu.cn/data/convert_bond_detail/{bond_code} 获取的HTML源代码
            bond_code: 可转债代码

        Returns:
            包含行业、地域、到期日、转债流通市值占比、相关公告列表的字典
        """
        try:
            soup = BeautifulSoup(html_content, "html.parser")
            result = {
                "bond_code": bond_code,
                "industry": "",
                "region": "",
                "maturity_date": "",
                "convert_amt_ratio": "",
                "announcements": [],
            }

            # 解析行业信息
            stock_indu_div = soup.find("div", class_="stock_indu")
            if stock_indu_div:
                industry_link = stock_indu_div.find("a", target="_cblist")
                if industry_link:
                    result["industry"] = industry_link.get_text(strip=True)

            # 解析地域信息
            province_td = soup.find("td", id="province")
            if province_td:
                result["region"] = province_td.get_text(strip=True)

            # 解析到期日
            maturity_td = soup.find("td", id="maturity_dt")
            if maturity_td:
                result["maturity_date"] = maturity_td.get_text(strip=True)

            # 解析转债流通市值占比
            convert_amt_ratio_td = soup.find("td", id="convert_amt_ratio")
            if convert_amt_ratio_td:
                result["convert_amt_ratio"] = convert_amt_ratio_td.get_text(strip=True)

            # 解析相关公告列表
            annos_div = soup.find("div", id="tbl_annos")
            if annos_div:
                grid_rows = annos_div.find_all("div", class_="grid-row")
                for row in grid_rows:
                    grid_col_9 = row.find("div", class_="grid-col-9")
                    grid_col_3 = row.find("div", class_="grid-col-3")

                    if grid_col_9 and grid_col_3:
                        announcement_link = grid_col_9.find("a")
                        if announcement_link:
                            announcement = {
                                "title": announcement_link.get_text(strip=True),
                                "url": announcement_link.get("href", ""),
                                "date": grid_col_3.get_text(strip=True),
                            }
                            result["announcements"].append(announcement)

            logger.info(
                f"成功解析可转债 {bond_code} 详情页: 行业={result['industry']}, 地域={result['region']}, 到期日={result['maturity_date']}, 流通市值占比={result['convert_amt_ratio']}, 公告数量={len(result['announcements'])}"
            )
            return result

        except Exception as e:
            logger.error(f"解析可转债 {bond_code} 详情页HTML异常: {e}")
            return {
                "bond_code": bond_code,
                "industry": "",
                "region": "",
                "maturity_date": "",
                "convert_amt_ratio": "",
                "announcements": [],
            }

    def get_convertible_bond_detail(self, bond_code: str) -> Dict[str, Any]:
        """
        获取可转债详情信息

        Args:
            bond_code: 可转债代码，如 '110092'

        Returns:
            包含行业、地域、相关公告列表的字典
        """
        try:
            url = f"https://www.jisilu.cn/data/convert_bond_detail/{bond_code}"
            logger.info(f"正在获取可转债 {bond_code} 详情页: {url}")

            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()

            # 解析HTML内容
            result = self.parse_convertible_bond_detail(response.text, bond_code)
            return result

        except Exception as e:
            logger.error(f"获取可转债 {bond_code} 详情信息异常: {e}")
            return {
                "bond_code": bond_code,
                "industry": "",
                "region": "",
                "maturity_date": "",
                "convert_amt_ratio": "",
                "announcements": [],
            }

    def filter_low_price_bonds(
        self, bonds_data: List[Dict[str, Any]], max_price: float = 114.0
    ) -> List[Dict[str, Any]]:
        """筛选价格低于指定值的可转债"""
        low_price_bonds = []

        # 定义有效的信用评级
        valid_credit_ratings = ["AAA", "AA+", "AA", "AA-", "A+", "A"]

        for bond in bonds_data:
            try:
                cell = bond.get("cell", {})
                price = cell.get("price")
                stock_price = cell.get("stock_price")
                credit_rating = cell.get("信用评级")
                premium_rt = cell.get("premium_rt")
                listing_time = cell.get("上市时间")

                # 新增过滤条件：
                # 1. 债现价低于最大价格
                # 2. 信用评级在指定列表中
                # 3. 正股价大于1元
                # 4. 转股溢价率不等于NaN
                # 5. 上市时间不等于NaT
                if (
                    price
                    and price != 100.0
                    and premium_rt != "nan"
                    and price < max_price
                    and credit_rating in valid_credit_ratings
                    and stock_price
                    and float(stock_price) > 1
                    and listing_time != "NaT"
                ):
                    low_price_bonds.append(
                        {
                            "代码": cell.get("bond_id", ""),
                            "转债名": cell.get("bond_nm", ""),
                            "价格": price,
                            "溢价率": cell.get("premium_rt", ""),
                            "转股价": cell.get("convert_price", ""),
                            "正股价": stock_price,
                            "正股代码": cell.get("正股代码", ""),
                            "正股简称": cell.get("正股简称", ""),  # 新增正股简称
                            "申购日期": cell.get("申购日期", ""),
                            "申购代码": cell.get("申购代码", ""),
                            "申购上限": cell.get("申购上限", ""),
                            "转股价值": cell.get("转股价值", ""),
                            "发行规模": cell.get("发行规模", ""),
                            "中签率": cell.get("中签率", ""),
                            "上市时间": cell.get("上市时间", ""),
                            "信用评级": credit_rating,
                        }
                    )
            except Exception as e:
                logger.warning(f"处理可转债数据异常: {e}")
                continue

        return low_price_bonds

    def format_message(self, bonds: List[Dict[str, Any]]) -> str:
        """格式化消息内容"""
        if not bonds:
            return "今日没有发现价格低于114的可转债"

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"🔔 A股可转债价格监控通知 ({current_time})\n\n"
        message += f"📊 发现 {len(bonds)} 只价格低于114的可转债：\n\n"

        # 按价格排序
        sorted_bonds = sorted(bonds, key=lambda x: x.get("溢价率", 0), reverse=True)

        for i, bond in enumerate(sorted_bonds, 1):
            bond_code = bond.get("代码", "")

            message += f"{i}. {bond_code} {bond.get('转债名', '')}\n"
            message += f"   正股代码: {bond.get('正股代码', '')} | 正股简称: {bond.get('正股简称', '')}\n"
            message += f"   价格: {bond.get('价格', 0):.2f} | 溢价率: {bond.get('溢价率', '')}%\n"
            message += f"   转股价: {bond.get('转股价', '')} | 正股价: {bond.get('正股价', '')}\n"
            message += f"   发行规模: {bond.get('发行规模', '')}亿元 | 信用评级: {bond.get('信用评级', '')}\n"

            # 获取可转债详情信息（行业、地域、公告）
            if bond_code:
                try:
                    detail_info = self.get_convertible_bond_detail(bond_code)
                    if detail_info:
                        # 添加行业和地域信息
                        industry = detail_info.get("industry", "")
                        region = detail_info.get("region", "")
                        maturity_date = detail_info.get("maturity_date", "")
                        convert_amt_ratio = detail_info.get("convert_amt_ratio", "")

                        if industry or region:
                            message += f"   行业: {industry} | 地域: {region}\n"

                        if maturity_date or convert_amt_ratio:
                            message += f"   到期日: {maturity_date} | 转债流通市值占比: {convert_amt_ratio}\n"

                        # 筛选包含"评级"字样的公告
                        announcements = detail_info.get("announcements", [])
                        rating_announcements = [
                            ann
                            for ann in announcements
                            if "评级" in ann.get("title", "")
                        ]

                        if rating_announcements:
                            message += f"   评级相关公告:\n"
                            # 只显示最新的2个评级公告
                            for ann in rating_announcements[:2]:
                                title = ann.get("title", "")
                                date = ann.get("date", "")
                                url = ann.get("url", "")
                                # 截断过长的标题
                                if len(title) > 60:
                                    title = title[:60] + "..."
                                # 如果有URL，创建可点击链接，否则只显示标题
                                if url:
                                    message += f"     • [{title}]({url}) ({date})\n"
                                else:
                                    message += f"     • {title} ({date})\n"

                except Exception as e:
                    logger.warning(f"获取可转债 {bond_code} 详情信息失败: {e}")

            message += "\n"

        return message

    def check_and_notify(self) -> None:
        """检查并发送通知"""
        try:
            logger.info("开始检查可转债数据...")

            # 获取可转债数据
            bonds_data = self.get_convertible_bonds_data()
            if not bonds_data:
                logger.warning("未获取到可转债数据")
                return

            # 筛选低价可转债
            low_price_bonds = self.filter_low_price_bonds(bonds_data)
            logger.info(f"发现 {len(low_price_bonds)} 只低价可转债")

            # 格式化消息
            message = self.format_message(low_price_bonds)

            # 发送飞书消息
            chat_id = os.getenv("FEISHU_CHAT_ID")  # 可选：指定群聊ID
            success = self.feishu.send_message(message, chat_id)

            if success:
                logger.info("飞书通知发送成功")
            else:
                logger.error("飞书通知发送失败")

        except Exception as e:
            logger.error(f"检查通知过程异常: {e}")
            import traceback

            traceback.print_exc()


def main():
    """主函数"""
    try:
        monitor = ConvertibleBondMonitor()

        # 立即执行一次
        logger.info("执行首次检查...")
        monitor.check_and_notify()

        # 设置定时任务：每个工作日早上9:30执行
        schedule.every().monday.at("09:30").do(monitor.check_and_notify)
        schedule.every().tuesday.at("09:30").do(monitor.check_and_notify)
        schedule.every().wednesday.at("09:30").do(monitor.check_and_notify)
        schedule.every().thursday.at("09:30").do(monitor.check_and_notify)
        schedule.every().friday.at("09:30").do(monitor.check_and_notify)

        logger.info("定时任务已设置，每个工作日早上9:30执行")
        logger.info("按 Ctrl+C 退出程序")

        # 运行定时任务
        while True:
            schedule.run_pending()
            time.sleep(60)  # 每分钟检查一次

    except KeyboardInterrupt:
        logger.info("程序已退出")
    except Exception as e:
        logger.error(f"程序运行异常: {e}")


if __name__ == "__main__":
    main()
