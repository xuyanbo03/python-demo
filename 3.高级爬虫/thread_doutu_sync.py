#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 同步爬虫，爬取斗图啦
import re
import os
import requests
from lxml import etree
from urllib import request

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Cookie': '__cfduid=de3fdac39558f42a35ea8095eedff18261571388629; UM_distinctid=16dde0fa1171af-0bf87dbcd275b5-b363e65-1fa400-16dde0fa1187f2; CNZZDATA1256911977=414509268-1571387222-%7C1571387222; XSRF-TOKEN=eyJpdiI6InFYMGp2d0R4b1h6MHVwWEd2aUU3c1E9PSIsInZhbHVlIjoiNUJtQlVGOGtnM2NUTE90N3BzTmp5eXRRenYzaGlMOGNoQ3pTYW9rNWZnS1dDRkpcL0psNHZ5WnJSaW9yK3ZWZXEiLCJtYWMiOiJjYTI2YjQ2M2Q0MjFhODJlYmFlNzU3YTUwOTc0NmE2N2JkOGRiMDVhNTIwMDI0YjlmZjFjY2JiMDE0YjU1MzFkIn0%3D; doutula_session=eyJpdiI6ImFoZjBHYTN3aHN1ZlcwTDdRN3UxeFE9PSIsInZhbHVlIjoiTENVQWdQejl6Vkh6dmNEandrZlQyWWJ0b3NYS3VFNjRCRkxGTmNPZkhaRWZYNzN6RStFeEZvWDdSNm9HNnBQVyIsIm1hYyI6IjBkNDViN2RhNWIwZmE4NWE1YWViMThlZjk0ZjM0NTExNmI5ZmQ3OTMzNWVlMjRiMmUyMzYwNDE2MzAyMGY3MGUifQ%3D%3D',
    'Host': 'www.doutula.com',
    'Referer': 'http://www.doutula.com/photo/list/?page=2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}


def parse_page(url):
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
    for img in imgs:
        img_url = img.get('data-original')
        alt = img.get('alt')
        alt = re.sub(r'[\?\.？。！，“”‘’@#￥%&*（）、\*]', '', alt)
        suffix = os.path.splitext((img_url))[1]
        filename = alt + suffix
        # print(img_url)
        # print(filename)
        request.urlretrieve(img_url, 'images/' + filename)


def main():
    for x in range(1, 101):
        url = 'http://www.doutula.com/photo/list/?page=%d' % x
        parse_page(url)
        break


if __name__ == '__main__':
    main()
