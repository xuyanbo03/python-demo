#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 多线程异步爬虫，爬取斗图啦
import re
import os
import requests
from lxml import etree
from urllib import request
from queue import Queue
import threading

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


class Producer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
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
            self.img_queue.put((img_url, filename))
            # print(img_url)
            # print(filename)
            # request.urlretrieve(img_url, 'images/' + filename)


class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty() and self.img_queue.empty():
                break
            img_url, filename = self.img_queue.get()
            request.urlretrieve(img_url, 'images/' + filename)
            print(filename + '  下载完成！')


def main():
    page_queue = Queue(50)
    img_queue = Queue(500)
    for x in range(1, 51):
        url = 'http://www.doutula.com/photo/list/?page=%d' % x
        page_queue.put(url)

    for x in range(5):
        t = Producer(page_queue, img_queue)
        t.start()
    for x in range(5):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == '__main__':
    main()
