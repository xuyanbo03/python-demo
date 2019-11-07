#!/usr/bin/python3
# -*- coding:utf-8 -*-
from scrapy import cmdline

# cmdline.execute("scrapy crawl qsbk_spider".split())
cmdline.execute(["scrapy", "crawl", "wxapp_spider"])
