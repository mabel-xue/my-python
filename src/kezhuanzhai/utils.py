import datetime
import requests


def output_excel(df, name):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{name}_{timestamp}.xlsx"
    df.to_excel(output_file, index=False)


def get_response(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    return requests.get(url, headers=headers).json()


def post_response(url, data):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    return requests.post(url, data, headers=headers)


def get_jsl_cookie():
    url = "https://www.jisilu.cn/webapi/account/login_process/"
    data = {
        "user_name": "a1496a9cb31188f8a708a18ca81e022b",
        "password": "c29ec670a83117e1359e656db05fe17f",
    }
    response = post_response(url, data)
    return response.headers.get("Set-Cookie")


jsl_cookie = ""
