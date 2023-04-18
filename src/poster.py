# -*- coding: utf-8 -*-

import requests
import time
import hashlib

# 构造请求头和请求参数
url = 'https://www.toutiao.com/pgc/ma/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.toutiao.com/c/user/token/MS4wLjABAAAAsamoDupqFwZFXmkFbrQpbvUMVxUwPMPdiBpm10HU2l0/?source=mine_home&tab=all',
    'cookie': 'd_ticket=0e688949b67ae3ef4e83be2348cc5685cc785; csrftoken=aa57591d6cd227ed6023916921fe0e09; _S_DPR=2; _S_IPAD=0; n_mh=hZ9bRfByXUjzmeTfIHytPnPrz5bXjD7s4QGoNYjZbmE; amp_d915a9=3vVm1Zk99-MJzQaI4uu7QC.M2h6VHJVbFVEeVRYYWtSZXowQmJGSG9TZlp3Mg==..1ghknedek.1ghknedkj.0.e.e; tt_webid=6910508120209606157; csrf_session_id=1398cbbd90cbc8e94042b1f361238067; notRedShot=1; _S_WIN_WH=1440_764; _ga=GA1.1.2047314707.1585980751; amp_adc4c4=a_BJ-yLvKBhVh73Yh7Nbfb.M2h6VHJVbFVEeVRYYWtSZXowQmJGSG9TZlp3Mg==..1gq6ittpq.1gq6j16bk.2.1u.20; passport_csrf_token=71c5f1becd8b93e7deef4ac96579ac1f; passport_csrf_token_default=71c5f1becd8b93e7deef4ac96579ac1f; sso_uid_tt=64bd4d21d1f94c4c5e495a33801af8cf; sso_uid_tt_ss=64bd4d21d1f94c4c5e495a33801af8cf; toutiao_sso_user=062724820e39ce75ec98db8fe0b647ae; toutiao_sso_user_ss=062724820e39ce75ec98db8fe0b647ae; sid_ucp_sso_v1=1.0.0-KGYwZmI3M2QxNTg0YTMwY2E5YzY3MWU5ODQ5NGMzODQyZWRlZjQ1N2IKHAiPmtbhFxDHiJigBhjPCSAMMLeT_bgFOAZA9AcaAmxxIiAwNjI3MjQ4MjBlMzljZTc1ZWM5OGRiOGZlMGI2NDdhZQ; ssid_ucp_sso_v1=1.0.0-KGYwZmI3M2QxNTg0YTMwY2E5YzY3MWU5ODQ5NGMzODQyZWRlZjQ1N2IKHAiPmtbhFxDHiJigBhjPCSAMMLeT_bgFOAZA9AcaAmxxIiAwNjI3MjQ4MjBlMzljZTc1ZWM5OGRiOGZlMGI2NDdhZQ; passport_auth_status=adcd676fa0645fc0374e9bf02c858f03%2C; passport_auth_status_ss=adcd676fa0645fc0374e9bf02c858f03%2C; sid_guard=5e81d4eb5d6b10cf40fba44b3e03ec62%7C1678115912%7C5183999%7CFri%2C+05-May-2023+15%3A18%3A31+GMT; uid_tt=5027bb28f2ec47643270ee2a5c5e5ace; uid_tt_ss=5027bb28f2ec47643270ee2a5c5e5ace; sid_tt=5e81d4eb5d6b10cf40fba44b3e03ec62; sessionid=5e81d4eb5d6b10cf40fba44b3e03ec62; sessionid_ss=5e81d4eb5d6b10cf40fba44b3e03ec62; sid_ucp_v1=1.0.0-KGJiZmEzMmI0ZTc4NWM2ZTA5Njg1ZWIwYzYxMmQwYmUxNGEzODM0NGQKFgiPmtbhFxDIiJigBhjPCSAMOAZA9AcaAmhsIiA1ZTgxZDRlYjVkNmIxMGNmNDBmYmE0NGIzZTAzZWM2Mg; ssid_ucp_v1=1.0.0-KGJiZmEzMmI0ZTc4NWM2ZTA5Njg1ZWIwYzYxMmQwYmUxNGEzODM0NGQKFgiPmtbhFxDIiJigBhjPCSAMOAZA9AcaAmhsIiA1ZTgxZDRlYjVkNmIxMGNmNDBmYmE0NGIzZTAzZWM2Mg; store-region=cn-bj; store-region-src=uid; local_city_cache=%E5%8C%97%E4%BA%AC; odin_tt=ff5480414ecbc24848ee10e14c7e15929ed7addd62dda5f2d93c1c56536f593a9d313f2d1810ee216aa6f324e37e1e4b; s_v_web_id=verify_lfsdvt0m_eBZ9961I_Fosz_4HaU_AZaF_MjhipclTLApi; msToken=dqSR7_JH6QEmTK-zj-ZB8a6jfOVj2Hdm6TxEI0SuOWQd4yZVHIav4RiVT4UIrRzpXBh031m3_fLFU6GoLUNFWVuVJhBU79F8nMVNrdkTLLk=; tt_anti_token=aU0xAKxpBpsZ9-28c354be326052741fa6810b1902370aa74d82db8a8ff5935fd4a25612aa5cd6; ttwid=1%7CG4kqz2MfJ8qDGRoMFM0lxLVzPLTri4e0xvMAYpgm5M8%7C1680354942%7C8b8f9fc280dece586808798e46e4b21bcfd131ad5a8a542ad390e8bde2620996; tt_scid=u45VbhlDj95ZyVqhAsmV0tGSqQotbKoKX3cNSs0A.lOwmPE07vJeg0PXmHm2AElxb239; _ga_QEHZPBE5HH=GS1.1.1680353719.45.1.1680355630.0.0.0',  # 请填写自己的cookie信息
    'x-requested-with': 'XMLHttpRequest'
}
params = {
    'category': 'profile_all',  # 请填写自己的自媒体user_id
    'utm_source': 'toutiao',
    'max_behot_time': '0',
    'ext': '{"query":"商业"}',
    'count': '20',
    'aid': '24',
    'format': 'json',
    'as': 'A1D51B7FCFDE335',
    'cp': '615DF24A8A1E9E1',
    'token': 'MS4wLjABAAAAsamoDupqFwZFXmkFbrQpbvUMVxUwPMPdiBpm10HU2l0',  # 请填写自己的token信息
    '_signature': '_02B4Z6wo00101NBR91QAAIDDRIesW5G9xnDQdfPAAFBBXnbEXSnm9Ow-Dw0bMrMzLenpz7tpEaiNAmuMF0AY4sGepiRqGDU9iQHTxPpYTtOawc7J3jBFxWFKJU4Kf-7RbJ4t9RU.sGhY-j.g18',  # 请填写自己的_signature信息
}

# 发送请求，获取文章列表
article_list = []
while True:
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    article_list += data['data']
    max_behot_time = data['next']['max_behot_time']
    params['max_behot_time'] = max_behot_time
    time.sleep(2)  # 设置访问间隔时间
    if not data['has_more']:
        break

# 打印文章列表
for article in article_list:
    print(article['title'])
