#!/usr/bin/python3
# -*- coding:utf-8 -*-
from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("tencent.html",parser=parser)

# 1. 获取所有ul标签
# uls = html.xpath("//ul")
# for ul in uls:
#     print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))

# 2. 获取第二个ul标签
# ul = html.xpath("//ul[@class='tableTr'][2]")[0]
# print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))

# 3.获取所有class 等于tableTr的ul标签
# uls = html.xpath("//ul[@class='tableTr']")
# for ul in uls:
#     print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))

# 4. 获取所有a标签的href属性
# aList = html.xpath("//ul//a/@href")
# for a in aList:
#     print('https://campus.alibaba.com' + a[1:])

# 5. 获取所有职位信息（纯文本）
uls = html.xpath("//ul[@class='tableTr']")
positions =[]
for ul in uls:
    href = ul.xpath(".//a/@href")[0]
    url = 'https://campus.alibaba.com' + href[1:]
    cate = ul.xpath(".//li/text()")[0]
    address = ul.xpath(".//li/text()")[1]
    pubtime = ul.xpath(".//li/text()")[2]
    title = ul.xpath(".//a/text()")[0]

    position = {
        'url':url,
        'cate':cate,
        'title':title,
        'address':address,
        'time':pubtime
    }
    positions.append(position)

print(positions)