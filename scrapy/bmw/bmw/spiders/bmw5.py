# -*- coding: utf-8 -*-
import scrapy
from bmw.items import BmwItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class Bmw5Spider(CrawlSpider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    rules = (
        Rule(LinkExtractor(
            allow=r"https://car.autohome.com.cn/pic/series/65.+"),
            callback="parse_page",
            follow=True
        ),
    )

    def parse_page(self, response):
        category = response.xpath("//div[@class='uibox']/div/text()").get()
        srcs = response.xpath("//div[contains(@class,'uibox-con')]/ul/li//img/@src").getall()
        srcs = list(map(lambda x: response.urljoin(x.replace("t_", "")), srcs))
        yield BmwItem(category=category, image_urls=srcs)

    def test_parse(self, response):
        uiboxs = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxs:
            category = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            # for url in urls:
            #     url = response.urljoin(url)
            #     print(url)
            urls = list(map(lambda url: response.urljoin(url), urls))
            item = BmwItem(category=category, image_urls=urls)
            yield item
