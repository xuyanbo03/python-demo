#!/usr/bin/python3
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar
from pyecharts import options as opts

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
ALL_DATA = []


def parse_page(url):
    resp = requests.get(url, headers=headers)
    text = resp.content.decode('utf-8')
    soup = BeautifulSoup(text, 'html5lib')
    conMidtab = soup.find('div', class_='conMidtab')
    tables = conMidtab.find_all('table')
    for tab in tables:
        trs = tab.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({'city': city, 'min_temp': int(min_temp)})
            # print(city, min_temp)


def main():
    base_url = 'http://www.weather.com.cn/textFC/{}.shtml'
    area = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn', 'gat']
    for x in area:
        url = base_url.format(x)
        parse_page(url)

    # 分析数据
    # 根据最低气温排序
    ALL_DATA.sort(key=lambda data: data['min_temp'])
    print(ALL_DATA)

    # 可视化
    data = ALL_DATA[0:10]
    cities = list(map(lambda x: x['city'], data))
    temps = list(map(lambda x: x['min_temp'], data))
    # chart = Bar('中国天气最低气温排行榜')
    # chart.add('', cities, temps)
    bar = (
        Bar()
            .add_xaxis(cities)
            .add_yaxis('城市',temps,category_gap="80%")
            .set_global_opts(title_opts=opts.TitleOpts(title="中国天气最低气温排行榜"))
    )
    bar.render('temperature.html')


if __name__ == '__main__':
    main()
