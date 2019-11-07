#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

# base_url = 'https://www.xicidaili.com/nn/1'
headers = {
    'Host': 'www.xicidaili.com',
    'Connection': 'keep-alive',
    'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',

    'Referer': 'https://www.xicidaili.com/wt',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTM3OGY4MjVmODY5OWZiYTU5YjAzYTFmYTliMzFjZjJlBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWJieEgraUpJUktMcWNjYm1OMzVTd0tVQzlQa09RRkpRSWRkRzdvR2xyN0E9BjsARg%3D%3D--a91a87836fd6f463bcd5edc4c22cf63bd7e71f99; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1570804432,1570871173,1571134685,1571233317; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1571233317'
}


def get_ip(url):
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'lxml')
    table = soup.find('table', id='ip_list')
    trs = table.find_all('tr')[1:]
    for tr in trs:
        ipinfo = list(tr.stripped_strings)
        ip = ipinfo[0] + ':' + ipinfo[1] + '\n'
		# ip = ipinfo[4].lower() + '://' + ipinfo[0] + ':' + ipinfo[1] + '\n'
    return ip


def spider():
    base_url = 'https://www.xicidaili.com/nn/{}'
    for x in range(1, 20):
        url = base_url.format(x)
        ip = get_ip(url)
        print(ip)
        with open('iplist.txt', 'a', encoding='utf-8') as f:
            f.write(ip)


if __name__ == '__main__':
    spider()
