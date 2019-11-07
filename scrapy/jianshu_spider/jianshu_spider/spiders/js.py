# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import ArticleSpiderItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        url = response.url
        url1 = url.split('?')[0]
        article_id = url1.split('/')[-1]
        title = response.xpath("//div[@class='_gp-ck']//h1[@class='_1RuRku']/text()").get()
        author = response.xpath("//span[@class='_22gUMi']/text()").get()
        pub_time = response.xpath("//div[@class='s-dsoj']//time/text()").get()
        word_count = response.xpath("//div[@class='s-dsoj']/span[last()-1]/text()").get().split()[1]
        read_count = response.xpath("//div[@class='s-dsoj']/span[last()]/text()").get().split()[1]
        like_count = response.xpath("//span[@class='_1GPnWJ'][1]/text()").get()
        content = response.xpath("//div[@class='_gp-ck']//article").get()

        avatar = response.xpath("//div[@class='_3Oo-T1']//img[@class='_3T9iJQ']/@src").get().split('?')[0]
        comment_count = response.xpath("//span[@class='_2R7vBo']/text()").get()
        subjects = ",".join(response.xpath("//div[@class='_2Nttfz']/a/span/text()").getall())

        item = ArticleSpiderItem(
            origin_url=url,
            article_id=article_id,
            title=title,
            author=author,
            avatar=avatar,
            pub_time=pub_time,
            word_count=word_count,
            read_count=read_count,
            like_count=like_count,
            comment_count=comment_count,
            subjects=subjects,
            content=content
        )
        yield item
