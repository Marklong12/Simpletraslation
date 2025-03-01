import requests
from hashlib import md5
import json
import random
from plyer import notification
import re
import time

def send_notification(source,answer):
    all_test=f'原句:{source}\n翻译:{answer}'
    for i in range(0,len(all_test),200):
        notification.notify(
        title='Baidu Translate',
        message=all_test[i:i+200],
        app_name='我的应用',
        timeout=10  # 持续时间（秒）
            )
        time.sleep(11)
        


def make_md5(s, encoding='utf-8'):
    """
    生成字符串的MD5哈希值。

    参数:
    s (str): 需要加密的字符串。
    encoding (str): 字符串编码，默认为 'utf-8'。

    返回:
    str: MD5哈希值的十六进制表示。
    """
    m5 = md5(s.encode(encoding)).hexdigest()
    return m5

def trans():
    # 百度翻译API的URL
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'

    # 应用ID和密钥，请替换为您的实际应用ID和密钥
    appid = 
    key = 

    # 源语言和目标语言
    from_lang = 'en'  # 英文
    to_lang = 'zh'    # 中文

    # 获取用户输入的原文本
    question = input("input origin text")

    # 生成随机数salt，用于签名
    salt = random.randint(32768, 65536)

    # 生成签名sign
    sign = make_md5(appid + question + str(salt) + key)
    """
    使用百度翻译API进行文本翻译。

    返回:
    tuple: 包含原始文本、翻译后的文本、源语言和目标语言的元组。
    """
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        'appid': appid,
        'q': question,
        'from': from_lang,
        'to': to_lang,
        'salt': salt,
        'sign': sign
    }

    # 发送GET请求到百度翻译API
    r = requests.get(url, params=payload, headers=headers)
    result = r.json()

    # 解析返回的JSON结果
    src = result['trans_result'][0]['src']
    dst = result['trans_result'][0]['dst']
    origin = result['from']
    to = result['to']

    # 打印翻译结果
    print(origin, to, src, dst)
    send_notification(src,dst)
    
    # 返回翻译结果
    return src, dst, origin, to

if __name__ == '__main__':
    trans() 
