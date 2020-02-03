#!/usr/bin/python3
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
html = '''
<div class="tableBody">
        <ul class="tableTr">
            <li class="tableTd width-signal" title="图形图像">图形图像</li>
            <li class="tableTd width-signal"><a
                    href="./projectDetail.htm?id=6&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F"
                    title="行业视觉理解与分析">行业视觉理解与分析</a></li>
            <li class="tableTd width-signal" title="杭州，北京">杭州，北京</li>
            <li class="tableTd width-middle">2020.01.01-2021.12.31</li>
            <li class="tableTd width-min detailOperate"><a
                    href="./projectDetail.htm?id=6&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F">查看详情</a>
            </li>
        </ul>
        <ul class="tableTr">
            <li class="tableTd width-signal" title="机器学习">机器学习</li>
            <li class="tableTd width-signal"><a
                    href="./projectDetail.htm?id=7&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F"
                    title="Large" scale="" cross="" domain="" recommendation="">Large scale Cross domain
                recommendation</a></li>
            <li class="tableTd width-signal" title="杭州">杭州</li>
            <li class="tableTd width-middle">2020.01.01-2022.07.23</li>
            <li class="tableTd width-min detailOperate"><a
                    href="./projectDetail.htm?id=7&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F">查看详情</a>
            </li>
        </ul>
        <ul class="tableTr">
            <li class="tableTd width-signal" title="自然语言处理">自然语言处理</li>
            <li class="tableTd width-signal"><a
                    href="./projectDetail.htm?id=8&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F"
                    title="电子商务领域的自然语言Query理解">电子商务领域的自然语言Query理解</a></li>
            <li class="tableTd width-signal" title="杭州">杭州</li>
            <li class="tableTd width-middle">2019.01.01-2021.07.29</li>
            <li class="tableTd width-min detailOperate"><a
                    href="./projectDetail.htm?id=8&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F">查看详情</a>
            </li>
        </ul>
        <ul class="tableTr">
            <li class="tableTd width-signal" title="搜索与推荐">搜索与推荐</li>
            <li class="tableTd width-signal"><a
                    href="./projectDetail.htm?id=9&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F"
                    title="推理算法系统">推理算法系统</a></li>
            <li class="tableTd width-signal" title="杭州">杭州</li>
            <li class="tableTd width-middle">2020.07.01-2023.12.31</li>
            <li class="tableTd width-min detailOperate"><a
                    href="./projectDetail.htm?id=9&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F">查看详情</a>
            </li>
        </ul>
        <ul class="tableTr">
            <li class="tableTd width-signal" title="自然语言处理">自然语言处理</li>
            <li class="tableTd width-signal"><a
                    href="./projectDetail.htm?id=10&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F"
                    title="Large" scale="" multimodal="" question-answering="" for="" e-commerce="" area="">Large Scale
                MultiModal Question-Answering for E-commerce Area</a></li>
            <li class="tableTd width-signal" title="杭州">杭州</li>
            <li class="tableTd width-middle">2019.01.01-2022.01.01</li>
            <li class="tableTd width-min detailOperate"><a
                    href="./projectDetail.htm?id=10&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F">查看详情</a>
            </li>
        </ul>
        <ul class="tableTr">
            <li class="tableTd width-signal" title="机器学习">机器学习</li>
            <li class="tableTd width-signal"><a
                    href="./projectDetail.htm?id=11&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F"
                    title="端上用户实时意图预测">端上用户实时意图预测</a></li>
            <li class="tableTd width-signal" title="杭州">杭州</li>
            <li class="tableTd width-middle">2019.12.01-2021.03.28</li>
            <li class="tableTd width-min detailOperate"><a
                    href="./projectDetail.htm?id=11&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F">查看详情</a>
            </li>
        </ul>
        <ul class="tableTr">
            <li class="tableTd width-signal" title="图形图像">图形图像</li>
            <li class="tableTd width-signal"><a
                    href="./projectDetail.htm?id=13&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F"
                    title="基于视觉数据的城市交通预测干预">基于视觉数据的城市交通预测干预</a></li>
            <li class="tableTd width-signal" title="杭州">杭州</li>
            <li class="tableTd width-middle">2019.01.01-2022.09.01</li>
            <li class="tableTd width-min detailOperate"><a
                    href="./projectDetail.htm?id=13&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F">查看详情</a>
            </li>
        </ul>
        <ul class="tableTr">
            <li class="tableTd width-signal" title="机器学习">机器学习</li>
            <li class="tableTd width-signal"><a
                    href="./projectDetail.htm?id=14&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F"
                    title="创新设计与元素形象的审美量化评估">创新设计与元素形象的审美量化评估</a></li>
            <li class="tableTd width-signal" title="北京">北京</li>
            <li class="tableTd width-middle">2020.01.01-2021.12.31</li>
            <li class="tableTd width-min detailOperate"><a
                    href="./projectDetail.htm?id=14&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F">查看详情</a>
            </li>
        </ul>
        <ul class="tableTr">
            <li class="tableTd width-signal" title="高性能计算">高性能计算</li>
            <li class="tableTd width-signal"><a
                    href="./projectDetail.htm?id=15&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F"
                    title="基于GPU等新硬件技术的计算引擎优化">基于GPU等新硬件技术的计算引擎优化</a></li>
            <li class="tableTd width-signal" title="北京">北京</li>
            <li class="tableTd width-middle">2019.01.01-2020.12.31</li>
            <li class="tableTd width-min detailOperate"><a
                    href="./projectDetail.htm?id=15&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F">查看详情</a>
            </li>
        </ul>
        <ul class="tableTr">
            <li class="tableTd width-signal" title="机器学习">机器学习</li>
            <li class="tableTd width-signal"><a
                    href="./projectDetail.htm?id=16&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F"
                    title="杂环境感知与自适应视觉算法">杂环境感知与自适应视觉算法</a></li>
            <li class="tableTd width-signal" title="杭州">杭州</li>
            <li class="tableTd width-middle">2019.02.01-2022.08.01</li>
            <li class="tableTd width-min detailOperate"><a
                    href="./projectDetail.htm?id=16&amp;batchId=82&amp;batchName=%E7%A0%94%E7%A9%B6%E5%9E%8B%E5%AE%9E%E4%B9%A0%E7%94%9F">查看详情</a>
            </li>
        </ul>
    </div>
'''

soup = BeautifulSoup(html,'lxml')

# 1. 获取所有ul标签
# uls = soup.find_all('ul')
# for ul in uls:
#     print(ul)

# 2. 获取第二个ul标签
# ul = soup.find_all('ul',limit=2)[1]
# print(ul)

# 3.获取所有class 等于tableTr的ul标签
# uls = soup.find_all('ul',class_='tableTr')
# for ul in uls:
#     print(ul)

# 4. 获取所有a标签的href属性
# aList = soup.find_all('a')
# for a in aList:
    # 1. 通过下标操作的方式
    # href = a['href']
    # print(href)
    # 2.通过attrs属性的方式
    # href = a.attrs['href']
    # print(href)

# 5. 获取所有职位信息（纯文本）
uls = soup.find_all('ul')
positions =[]
for ul in uls:
    # 1. 按照string获取
    # lis = ul.find_all('li')
    # href = lis[1].find('a')['href']
    # url = 'https://campus.alibaba.com' + href[1:]
    # cate = lis[0].string
    # title = lis[1].string
    # address = lis[2].string
    # pubtime = lis[3].string
    # position = {
    #     'url':url,
    #     'cate':cate,
    #     'title':title,
    #     'address':address,
    #     'time':pubtime
    # }
    # positions.append(position)

    # 2. 按照stripped_strings获取
    infos = list(ul.stripped_strings)
    position = {
        'cate':infos[0],
        'title':infos[1],
        'address':infos[2],
        'time':infos[3]
    }
    positions.append(position)

print(positions)