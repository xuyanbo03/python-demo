#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 分析拉勾网ajax接口，直接请求接口，获取数据
import requests
from lxml import etree
import time
import random
import json
import re

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '_ga=GA1.2.999283199.1570804612; user_trace_token=20191011223651-90869f06-ec34-11e9-9a49-525400f775ce; LGUID=20191011223651-9086a272-ec34-11e9-9a49-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.931800981.1571411786; JSESSIONID=ABAAABAAAGFABEFB7E309ADD3DADC23DFAEA64165271488; WEBTJ-ID=20191019110520-16de1fa00291a4-06f7275f18368d-b363e65-2073600-16de1fa002a2e6; X_HTTP_TOKEN=5e3df2106f92bc530234541751c332fa8f9e1a1be7; _gat=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216dbb4086162b5-05733d0c28d29b-67e1b3f-921600-16dbb4086171c1%22%2C%22%24device_id%22%3A%2216dbb4086162b5-05733d0c28d29b-67e1b3f-921600-16dbb4086171c1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570804682,1570869595,1571411786,1571454323; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1571454323; LGSID=20191019110522-4a0df999-f21d-11e9-9ec1-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_java%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE%3Foquery%3DHadoop%26fromSearch%3Dtrue%26labelWords%3Drelative; LGRID=20191019110522-4a0dfd21-f21d-11e9-9ec1-525400f775ce; SEARCH_ID=12dbf2888a78422a839d579335f52ad1',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.lagou.com/jobs/list_java%E5%A4%A7%E6%95%B0%E6%8D%AE?oquery=Hadoop&fromSearch=true&labelWords=relative',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'
}


def parse_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    data = {
        'first': 'true',
        'pn': '1',
        'kd': 'java大数据'
    }
    # response = requests.post(url, headers=headers, data=data)
    # print(response.json())
    # time.sleep(random.randint(1, 10))
    with open('lagou.json', 'r', encoding='utf-8') as fp:
        response = json.load(fp)
    # print(response)
    positions = response['content']['positionResult']['result']
    for position in positions:
        position_id = position['positionId']
        position_url = 'https://www.lagou.com/jobs/%s.html' % position_id
        parse_position_detail(position_url)
        break


def parse_position_detail(url):
    # response = requests.get(url, headers=headers)
    # print(response.content.decode('utf-8'))
    with open('lagou.html', 'r', encoding='utf-8') as fp:
        text = fp.read()
    # print(text)
    html = etree.HTML(text)
    position_name = html.xpath("//div[@class='job-name']/h1[@class='name']/text()")[0]
    job_requests_spans = html.xpath("//dd[@class='job_request']//span")
    salary = job_requests_spans[0].xpath(".//text()")[0].strip()
    city = job_requests_spans[1].xpath(".//text()")[0].strip()
    city = re.sub(r'[\s/]', '', city)
    work_years = job_requests_spans[2].xpath(".//text()")[0].strip()
    work_years = re.sub(r'[\s/]', '', work_years)
    education = job_requests_spans[3].xpath(".//text()")[0].strip()
    education = re.sub(r'[\s/]', '', education)
    desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
    print(desc)


if __name__ == '__main__':
    parse_page()
