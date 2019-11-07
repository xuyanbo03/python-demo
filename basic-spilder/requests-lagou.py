#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

headers = {
    'Cookie':'_ga=GA1.2.999283199.1570804612; _gid=GA1.2.865629358.1570804612; user_trace_token=20191011223651-90869f06-ec34-11e9-9a49-525400f775ce; LGUID=20191011223651-9086a272-ec34-11e9-9a49-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216dbb4086162b5-05733d0c28d29b-67e1b3f-921600-16dbb4086171c1%22%2C%22%24device_id%22%3A%2216dbb4086162b5-05733d0c28d29b-67e1b3f-921600-16dbb4086171c1%22%7D; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGGABCBC1BFCCE09123AF3DAD9710F4D260A8A0; WEBTJ-ID=20191012163954-16dbf1fc9ed181-08208a9393e91a-67e1b3f-921600-16dbf1fc9ee102; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570804612,1570804682,1570869595; _gat=1; LGSID=20191012163954-dd5d85f9-eccb-11e9-a57b-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=5e3df2106f92bc537069680751c332fa8f9e1a1be7; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570869608; LGRID=20191012164007-e4f6abca-eccb-11e9-a57b-5254005c3644; SEARCH_ID=6ab3c2c5ce934ac49fc10ee534d9f21c',
    'Origin': 'https://www.lagou.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.lagou.com/jobs/list_%E5%A4%A7%E6%95%B0%E6%8D%AE?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

data = {
    'first': 'true',
    'pn': 1,
    'kd': '大数据'
}

proxy = {
    'http':'27.152.90.44:9999'
}

resp = requests.post(url,data=data,headers=headers,proxies=proxy)
print(resp.text)