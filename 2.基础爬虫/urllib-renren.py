#!/usr/bin/python3
# -*- coding:utf-8 -*-

from http.cookiejar import CookieJar
from urllib import request, parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}


def get_opener():
    cookiejar = CookieJar()
    handler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)
    return opener


def login_renren(opener):
    data = {
        'email': '',
        'password': ''
    }
    data = parse.urlencode(data).encode('utf-8')
    login_url = 'http://www.renren.com/PLogin.do'
    req = request.Request(login_url, headers=headers, data=data)
    opener.open(req)


def visit_profile(opener):
    dapeng_url = 'http://www.renren.com/880151247/profile'
    req = request.Request(dapeng_url, headers=headers)
    resp = opener.open(req)
    with open('renren.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))


if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)
