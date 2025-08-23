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
from typing import List, Dict, Any, Tuple
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

    def send_webhook_message(self, content: str, card_content: dict = None) -> bool:
        """通过webhook发送消息"""
        try:
            # 如果提供了卡片内容，使用卡片消息
            if card_content:
                data = {"msg_type": "interactive", "card": card_content}
            else:
                # 保留原有的文本消息发送逻辑
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

    def send_message(
        self, content: str, chat_id: str = None, card_content: dict = None
    ) -> bool:
        """发送消息"""
        if self.webhook_url:
            return self.send_webhook_message(content, card_content)
        elif chat_id and self.access_token:
            # TODO: 实现API发送卡片消息的逻辑
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

        # 观察池 - 需要特别关注的可转债代码列表
        # 可以通过环境变量WATCH_BOND_CODES配置，多个代码用逗号分隔，如: "110092,113025,128136"
        watch_codes_env = os.getenv("WATCH_BOND_CODES", "")
        self.watch_pool = (
            [code.strip() for code in watch_codes_env.split(",") if code.strip()]
            if watch_codes_env
            else []
        )

        if self.watch_pool:
            logger.info(
                f"观察池已配置，包含 {len(self.watch_pool)} 只可转债: {', '.join(self.watch_pool)}"
            )
        else:
            logger.info("观察池为空，可通过环境变量WATCH_BOND_CODES配置")

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
        解析可转债详情页HTML源代码，提取行业、地域、到期日、转债流通市值占比、价格、正股PB、相关公告信息

        Args:
            html_content: 从 https://www.jisilu.cn/data/convert_bond_detail/{bond_code} 获取的HTML源代码
            bond_code: 可转债代码

        Returns:
            包含行业、地域、到期日、转债流通市值占比、价格、正股PB、相关公告列表的字典
        """
        try:
            soup = BeautifulSoup(html_content, "html.parser")
            result = {
                "bond_code": bond_code,
                "industry": "",
                "region": "",
                "maturity_date": "",
                "convert_amt_ratio": "",
                "bond_price": "",
                "stock_pb": "",
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

            # 解析转债价格
            # 查找包含"价格"文字的td，然后提取其中span标签的内容
            price_tds = soup.find_all("td", class_="jisilu_subtitle")
            for td in price_tds:
                if "价格" in td.get_text():
                    price_span = td.find("span")
                    if price_span:
                        result["bond_price"] = price_span.get_text(strip=True)
                    break

            # 解析正股PB
            # 查找包含"正股PB"文字的td，然后查找紧邻的data_val类td
            pb_title_tds = soup.find_all("td", class_="jisilu_title")
            for td in pb_title_tds:
                if "正股PB" in td.get_text():
                    # 查找同一行的下一个data_val类td
                    next_td = td.find_next_sibling("td", class_="data_val")
                    if next_td:
                        result["stock_pb"] = next_td.get_text(strip=True)
                    break

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
                f"成功解析可转债 {bond_code} 详情页: 行业={result['industry']}, 地域={result['region']}, 到期日={result['maturity_date']}, 流通市值占比={result['convert_amt_ratio']}, 价格={result['bond_price']}, 正股PB={result['stock_pb']}, 公告数量={len(result['announcements'])}"
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
                "bond_price": "",
                "stock_pb": "",
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
                "bond_price": "",
                "stock_pb": "",
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

    def format_message(self, bonds: List[Dict[str, Any]]) -> Tuple[str, dict]:
        """格式化消息内容，返回文本消息和卡片消息"""
        if not bonds:
            return "今日没有发现价格低于114的可转债", None

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text_message = f"🔔 A股可转债价格监控通知 ({current_time})\n\n"
        text_message += f"📊 发现 {len(bonds)} 只价格低于114的可转债：\n\n"

        # 按溢价率排序
        sorted_bonds = sorted(
            bonds, key=lambda x: float(x.get("溢价率", 0)), reverse=True
        )

        # 飞书卡片消息结构
        card_content = {
            "config": {"wide_screen_mode": True},
            "header": {
                "title": {
                    "content": f"🔔 A股可转债价格监控通知 ({current_time})",
                    "tag": "plain_text",
                },
                "template": "blue",
            },
            "elements": [],
        }

        for i, bond in enumerate(sorted_bonds, 1):
            bond_code = bond.get("代码", "")
            bond_name = bond.get("转债名", "")
            is_watching = bond_code in self.watch_pool

            # 文本消息部分
            if is_watching:
                text_message += f"{i}. **{bond_code} {bond_name}** (监控中)\n"
            else:
                text_message += f"{i}. {bond_code} {bond_name}\n"

            text_message += f"   正股代码: {bond.get('正股代码', '')} | 正股简称: {bond.get('正股简称', '')}\n"
            text_message += f"   价格: {bond.get('价格', 0):.2f} | 溢价率: {bond.get('溢价率', '')}%\n"
            text_message += f"   转股价: {bond.get('转股价', '')} | 正股价: {bond.get('正股价', '')}\n"
            text_message += f"   发行规模: {bond.get('发行规模', '')}亿元 | 信用评级: {bond.get('信用评级', '')}\n\n"

            # 卡片消息部分
            bond_detail_text = []

            # 基本信息
            bond_detail_text.append(
                f"**{bond_code} {bond_name}** {'🚨 (监控中)' if is_watching else ''}"
            )
            bond_detail_text.append(
                f"正股代码: {bond.get('正股代码', '')} | 正股简称: {bond.get('正股简称', '')}"
            )
            bond_detail_text.append(
                f"价格: {bond.get('价格', 0):.2f} | 溢价率: {bond.get('溢价率', '')}% | 转股价: {bond.get('转股价', '')} | 正股价: {bond.get('正股价', '')}"
            )
            bond_detail_text.append(
                f"发行规模: {bond.get('发行规模', '')}亿元 | 信用评级: {bond.get('信用评级', '')}"
            )

            # 获取可转债详情信息
            if bond_code:
                try:
                    detail_info = self.get_convertible_bond_detail(bond_code)
                    if detail_info:
                        industry = detail_info.get("industry", "")
                        region = detail_info.get("region", "")
                        maturity_date = detail_info.get("maturity_date", "")
                        convert_amt_ratio = detail_info.get("convert_amt_ratio", "")

                        if industry or region:
                            bond_detail_text.append(
                                f"行业: {industry} | 地域: {region}"
                            )

                        if maturity_date or convert_amt_ratio:
                            bond_detail_text.append(
                                f"到期日: {maturity_date} | 转债流通市值占比: {convert_amt_ratio}"
                            )

                        # 处理评级公告
                        announcements = detail_info.get("announcements", [])
                        rating_announcements = [
                            ann
                            for ann in announcements
                            if "评级" in ann.get("title", "")
                        ]

                        if rating_announcements:
                            bond_detail_text.append("**评级相关公告:**")
                            for ann in rating_announcements[:2]:
                                title = ann.get("title", "")
                                date = ann.get("date", "")
                                url = ann.get("url", "")

                                # 截断过长的标题
                                if len(title) > 60:
                                    title = title[:60] + "..."

                                # 如果有URL，创建可点击链接
                                if url:
                                    bond_detail_text.append(
                                        f"• [{title}]({url}) ({date})"
                                    )
                                else:
                                    bond_detail_text.append(f"• {title} ({date})")

                except Exception as e:
                    logger.warning(f"获取可转债 {bond_code} 详情信息失败: {e}")

            # 创建卡片的文本模块
            card_content["elements"].append(
                {"tag": "markdown", "content": "\n".join(bond_detail_text)}
            )

            # 添加分隔线
            card_content["elements"].append({"tag": "hr"})

        return text_message, card_content

    def query_bonds_by_names(self, bond_names: List[str]) -> List[Dict[str, Any]]:
        """
        根据可转债名称数组查询可转债信息
        
        Args:
            bond_names: 可转债名称列表
            
        Returns:
            包含代码/行业/现价/转债流通市值占比/正股PB/到期时间信息的列表，按到期时间升序排列
        """
        try:
            logger.info(f"开始查询可转债: {', '.join(bond_names)}")
            
            # 获取所有可转债数据
            all_bonds_data = self.get_convertible_bonds_data()
            if not all_bonds_data:
                logger.warning("未获取到可转债数据")
                return []
            
            # 根据名称筛选可转债
            matched_bonds = []
            for bond in all_bonds_data:
                try:
                    cell = bond.get("cell", {})
                    bond_nm = cell.get("bond_nm", "").strip()
                    
                    # 检查是否匹配输入的名称
                    for target_name in bond_names:
                        if target_name.strip() in bond_nm or bond_nm in target_name.strip():
                            bond_code = cell.get("bond_id", "").strip()
                            
                            # 获取详细信息
                            detail_info = self.get_convertible_bond_detail(bond_code)
                            
                            bond_info = {
                                "代码": bond_code,
                                "转债名": bond_nm,
                                "行业": detail_info.get("industry", ""),
                                "现价": cell.get("price", 0),
                                "转债流通市值占比": detail_info.get("convert_amt_ratio", ""),
                                "正股PB": detail_info.get("stock_pb", ""),
                                "到期时间": detail_info.get("maturity_date", ""),
                                "正股代码": cell.get("正股代码", ""),
                                "正股简称": cell.get("正股简称", ""),
                                "转股价": cell.get("convert_price", ""),
                                "正股价": cell.get("stock_price", ""),
                                "溢价率": cell.get("premium_rt", ""),
                                "信用评级": cell.get("信用评级", ""),
                            }
                            
                            matched_bonds.append(bond_info)
                            logger.info(f"找到匹配的可转债: {bond_nm} ({bond_code})")
                            break
                            
                except Exception as e:
                    logger.warning(f"处理可转债数据异常: {e}")
                    continue
            
            # 按到期时间升序排列
            def parse_maturity_date(date_str):
                """解析到期日期字符串为datetime对象，用于排序"""
                if not date_str or date_str == "":
                    return datetime.max  # 无到期日期的放在最后
                try:
                    # 尝试解析不同的日期格式
                    for fmt in ["%Y-%m-%d", "%Y/%m/%d", "%Y.%m.%d"]:
                        try:
                            return datetime.strptime(date_str, fmt)
                        except ValueError:
                            continue
                    return datetime.max
                except:
                    return datetime.max
            
            matched_bonds.sort(key=lambda x: parse_maturity_date(x.get("到期时间", "")))
            
            logger.info(f"成功查询到 {len(matched_bonds)} 只匹配的可转债")
            return matched_bonds
            
        except Exception as e:
            logger.error(f"查询可转债异常: {e}")
            return []

    def format_bonds_query_message(self, bonds: List[Dict[str, Any]]) -> Tuple[str, dict]:
        """格式化查询结果消息内容，返回文本消息和卡片消息"""
        if not bonds:
            return "未找到匹配的可转债信息", None

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text_message = f"🔍 可转债查询结果 ({current_time})\n\n"
        text_message += f"📊 找到 {len(bonds)} 只可转债信息（按到期时间升序）：\n\n"

        # 飞书卡片消息结构
        card_content = {
            "config": {"wide_screen_mode": True},
            "header": {
                "title": {
                    "content": f"🔍 可转债查询结果 ({current_time})",
                    "tag": "plain_text",
                },
                "template": "green",
            },
            "elements": [],
        }

        for i, bond in enumerate(bonds, 1):
            bond_code = bond.get("代码", "")
            bond_name = bond.get("转债名", "")

            # 文本消息部分
            text_message += f"{i}. {bond_code} {bond_name}\n"
            text_message += f"   行业: {bond.get('行业', '')} | 现价: {bond.get('现价', 0):.2f}\n"
            text_message += f"   转债流通市值占比: {bond.get('转债流通市值占比', '')} | 正股PB: {bond.get('正股PB', '')}\n"
            text_message += f"   到期时间: {bond.get('到期时间', '')} | 信用评级: {bond.get('信用评级', '')}\n"
            text_message += f"   正股: {bond.get('正股代码', '')} {bond.get('正股简称', '')} ({bond.get('正股价', '')})\n"
            text_message += f"   转股价: {bond.get('转股价', '')} | 溢价率: {bond.get('溢价率', '')}%\n\n"

            # 卡片消息部分
            bond_detail_text = []
            
            # 基本信息
            bond_detail_text.append(f"**{bond_code} {bond_name}**")
            bond_detail_text.append(f"行业: {bond.get('行业', '')} | 现价: **{bond.get('现价', 0):.2f}**")
            bond_detail_text.append(f"转债流通市值占比: {bond.get('转债流通市值占比', '')} | 正股PB: {bond.get('正股PB', '')}")
            bond_detail_text.append(f"到期时间: **{bond.get('到期时间', '')}** | 信用评级: {bond.get('信用评级', '')}")
            bond_detail_text.append(f"正股: {bond.get('正股代码', '')} {bond.get('正股简称', '')} ({bond.get('正股价', '')})")
            bond_detail_text.append(f"转股价: {bond.get('转股价', '')} | 溢价率: {bond.get('溢价率', '')}%")

            # 创建卡片的文本模块
            card_content["elements"].append(
                {"tag": "markdown", "content": "\n".join(bond_detail_text)}
            )

            # 添加分隔线
            if i < len(bonds):
                card_content["elements"].append({"tag": "hr"})

        return text_message, card_content

    def query_and_notify_bonds(self, bond_names: List[str]) -> None:
        """根据可转债名称查询并发送飞书通知"""
        try:
            logger.info(f"开始查询并通知可转债: {', '.join(bond_names)}")

            # 查询可转债信息
            bonds_info = self.query_bonds_by_names(bond_names)
            if not bonds_info:
                logger.warning("未找到匹配的可转债信息")
                return

            # 格式化消息
            text_message, card_content = self.format_bonds_query_message(bonds_info)

            # 发送飞书消息
            chat_id = os.getenv("FEISHU_CHAT_ID")
            success = self.feishu.send_message(text_message, chat_id, card_content)

            if success:
                logger.info("飞书查询结果通知发送成功")
            else:
                logger.error("飞书查询结果通知发送失败")

        except Exception as e:
            logger.error(f"查询并通知过程异常: {e}")
            import traceback
            traceback.print_exc()

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
            text_message, card_content = self.format_message(low_price_bonds)

            # 发送飞书消息
            chat_id = os.getenv("FEISHU_CHAT_ID")  # 可选：指定群聊ID
            success = self.feishu.send_message(text_message, chat_id, card_content)

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
        # 设置需要监控的可转债代码
        os.environ["WATCH_BOND_CODES"] = (
            "128108,127025"  # 示例代码，可以根据实际需求修改
        )

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
