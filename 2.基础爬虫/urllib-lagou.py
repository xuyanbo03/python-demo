#!/usr/bin/python3
# -*- coding:utf-8 -*-

from urllib import request, parse

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%AE%9E%E4%B9%A0?labelWords=sug&fromSearch=true&suginput=%E5%A4%A7%E6%95%B0%E6%8D%AE'
}

data = {
    'first': 'true',
    'pn': 1,
    'kd': '大数据实习'
}
data = parse.urlencode(data).encode('utf-8')

handler = request.ProxyHandler({'http':'27.152.90.44:9999'})
opener = request.build_opener(handler)
req = request.Request('http://httpbin.org/ip')
# resp = opener.open(req)

# req = request.Request(url, headers=headers, data=data, method='POST')
# resp = request.urlopen(req)
resp = opener.open(req)
print(resp.read().decode('utf-8'))
