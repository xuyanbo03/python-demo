#!/usr/bin/python3
# -*- coding:utf-8 -*-

import requests

kw = {'wd': '中国'}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

response = requests.get("http://www.baidu.com/s", params=kw, headers=headers)

with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode('utf-8'))

print(response.url)
