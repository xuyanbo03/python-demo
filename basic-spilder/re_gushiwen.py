#!/usr/bin/python3
# -*- coding:utf-8 -*-
import re
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}


def parse_page(url):
    response = requests.get(url, headers=headers)
    text = response.text
    titles = re.findall(r'class="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
    dynasties = re.findall(r'class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    authors = re.findall(r'class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    contents_tags = re.findall(r'class="contson".*?>(.*?)</div>', text, re.DOTALL)
    contents = []
    for c in contents_tags:
        x = re.sub(r'<.*?>', '', c, re.DOTALL)
        contents.append(x.strip())
    # print(contents)

    poems = []
    for val in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = val
        poem = {
            'title' : title,
            'dynasty' : dynasty,
            'author':author,
            'content' : content
        }
        poems.append(poem)
    for poem in poems:
        print(poem)
        print('='*30)


def main():
    url = 'https://www.gushiwen.org/default_1.aspx'
    parse_page(url)


if __name__ == '__main__':
    main()
