#!/usr/bin/python3
# -*- coding:utf-8 -*-
from time import sleep
import requests
from urllib import parse
from bs4 import BeautifulSoup
from lxml import etree

base_url = 'https://www.qichacha.com'
headers = {
    'Host': 'www.qichacha.com',
    'Connection': 'keep-alive',
    'Accept': r'text/html, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',

    'Referer': 'https://www.qichacha.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Cookie': 'QCCSESSID=5inph6i4hu8gsgpukolakkgfd7; zg_did=%7B%22did%22%3A%20%2216dd3efe48712c-019499eb3fec11-b363e65-1fa400-16dd3efe48c258%22%7D; UM_distinctid=16dd3efe4de43-0b9f7570be9b8-b363e65-1fa400-16dd3efe4df799; CNZZDATA1254842228=708558580-1571217716-https%253A%252F%252Fwww.baidu.com%252F%7C1571217716; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1571218777; hasShow=1; _uab_collina=157121877756639787849244; acw_tc=df6ff44615712187766106257e39c45d863eada42f74991f22af6b0ea9; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201571218777233%2C%22updated%22%3A%201571220992862%2C%22info%22%3A%201571218777237%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1571220993'
}


def get_link(url):
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'lxml')
    a = soup.find('a', class_='ma_h1')
    href = a['href']
    detail_url = base_url + href
    return detail_url


def get_name(url):
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'lxml')
    table = soup.find('table', class_='ntable')
    tr = table.find_all('tr')[8]
    name = list(tr.stripped_strings)[1]
    return name


def spider():
    lists = ['百度', '阿里巴巴', '腾讯']
    for l in lists:
        data = {
            'key': l
        }
        qs = parse.urlencode(data)
        url = base_url + '/search?' + qs
        detail_url = get_link(url)
        name = get_name(detail_url)
        print(name)
        sleep(1)


if __name__ == '__main__':
    spider()
