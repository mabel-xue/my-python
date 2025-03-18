import time
from bs4 import BeautifulSoup
import requests
import schedule

GROUP_URL = "https://www.douban.com/group/lala/?joining_pop=1"  # 替换为你的豆瓣小组链接
COOKIES = {"bid": "mF6bMQ_KWno"}


HEADER_1 = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}

HEADER_2 = {
    "Cookie": '__utmv=30149280.14513; _ga_RXNMP372GL=GS1.1.1711034587.1.1.1711034879.60.0.0; viewed="27049704_25717380_25833225_19952397_34861737_27108685_26862694_26289656_6439420_35124662"; bid=GiWey58i4VE; ll="108288"; _pk_id.100001.8cb4=2673e6c8bbfd9f90.1724073161.; __utmc=30149280; __utmz=30149280.1724073163.14.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="145133188:/kwCT+NrflY"; ck=nQze; frodotk_db="63f3c13cbb64dccf2bdb43b6322e966d"; ct=y; push_noty_num=0; push_doumail_num=0; _ga=GA1.2.1331631967.1711034371; _ga_Y4GN1R87RG=GS1.1.1724415931.4.0.1724415938.0.0.0; ap_v=0,6.0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1725009468%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dx7YmZcaHELVfZZHOMi64Omlhliq07Rh34jHHqQWPnfQjLInQz_nBVtrI_whjr3Wx%26wd%3D%26eqid%3Dc342dfc6000082460000000366c344bc%22%5D; _pk_ses.100001.8cb4=1; __utma=30149280.516241902.1682590651.1724680416.1725009469.24; __utmt=1; __utmb=30149280.75.4.1725010350149',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}


def get_soup(url, headers=None):
    rsp = requests.get(url, headers=headers)
    rsp.raise_for_status()
    html = rsp.text
    soup = BeautifulSoup(html, "html.parser")
    return soup


def check_group_and_comment():
    # 刷新小组首页
    soup = get_soup(GROUP_URL, HEADER_1)
    rows = soup.find("table", {"class": "olt"}).find_all("tr")
    print("start")
    for item in rows:
        titleDiv = item.find("td", {"class": "title"})
        if titleDiv:
            target = titleDiv.find("a")
            title = target.text
            link = target.get("href")
            if "群招" in title and "适合拥抱的" in title:
                print("找到帖子：", title)
                image_path = "/Users/mabelxue/Downloads/my-python/src/gm.jpg"
                with open(image_path, "rb") as img:
                    # print(image_path)
                    comment_data = {
                        "rv_comment": "北京GirlMatch心动试验——第三期\n● 深度聊天、谈话、小游戏多维度环节穿插\n● 全程主持控场，i人极度适配\n● 场地宠物友好，狗子也能欢乐玩耍\n● 活动内容质量高，环节逐渐升温，带你顺利破圈\n📮 活动时间：9-16下午14:00-19:00 （中秋第二天）\n🏞️ 活动地点：丰台区槐新公园\n🎉 活动内容概览：\n● 集合签到、暖场\n● 趣味游戏第一趴\n● 定向主题聊天交流\n● 趣味游戏第二趴\n● 帮帮问\n🙋🏻‍♀️ 活动预计人数：12-15人 年龄要求：25+",
                        "start": "400",
                        "ck": "nQze",
                        "submit_btn": "发送",
                    }
                    files = {"img": img}  # This is where the image file is added
                    comment_response = requests.post(
                        link + "/add_comment",
                        data=comment_data,
                        files=files,
                        headers=HEADER_2,
                    )
                    if comment_response.status_code == 200:
                        print("成功留言")
                        return schedule.CancelJob

                    else:
                        print("留言失败", comment_response.text)


# 设置定时任务
# schedule.every(1).minutes.do(check_group_and_comment)  # 每10分钟执行一次

# while True:
#     schedule.run_pending()
#     time.sleep(1)

check_group_and_comment()
