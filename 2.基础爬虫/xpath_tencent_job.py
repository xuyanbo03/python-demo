#!/usr/bin/python3
# -*- coding:utf-8 -*-
from lxml import etree
import requests

BASE_URL = 'https://careers.tencent.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Referer': 'https://careers.tencent.com/search.html?query=ot_40001001,ot_40001003,ot_40001005,at_1,ci_3,co_1&index=16'
}


def get_detail_urls(url):
    resp = requests.get(url, headers=headers)
    text = resp.text
    # text = resp.content.decode('gbk')
    # with open('dytt.html','w',encoding='gbk') as f:
    #     f.write(text)
    htmlE = etree.HTML(text)
    detail_urls = htmlE.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url: BASE_URL + url, detail_urls)
    return detail_urls


def parse_detail_page(url):
    movie = {}
    resp = requests.get(url, headers=headers)
    text = resp.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]
    screenshot = imgs[1]
    movie['cover'] = cover
    movie['screenshot'] = screenshot

    def parse_info(info, rule):
        return info.replace(rule, '').strip()

    infos = zoomE.xpath(".//text()")
    for index, info in enumerate(infos):
        if info.startswith("◎年　　代"):
            info = parse_info(info, "◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info, "◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info, "◎类　　别")
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info, "◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info, "◎片　　长")
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info, "◎导　　演")
            movie['director'] = info
        elif info.startswith("◎主　　演"):
            info = parse_info(info, "◎主　　演")
            actors = [info]
            for x in range(index + 1, len(infos)):
                actor = infos[x].strip()
                if actor.startswith('◎'):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            info = parse_info(info, "◎简　　介")
            profiles = ''
            for x in range(index + 1, len(infos)):
                profile = infos[x].strip()
                if profile.startswith('【'):
                    break
                profiles += profile
            movie['profile'] = profiles

    download_url = zoomE.xpath(".//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url
    return movie


def spider():
    list_url = 'https://careers.tencent.com/search.html?query=ot_40001001,ot_40001003,ot_40001005,at_1,ci_3,co_1&index={}'
    jobs = []
    for x in range(1, 17):
        url = list_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            job = parse_detail_page(detail_url)
            jobs.append(job)
            print(job)


if __name__ == '__main__':
    spider()
