# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem


class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101190400/?query=Java&page=1&ka=page-1']

    rules = (
        Rule(LinkExtractor(allow=r'.+\?query=Java&page=\d&ka=page-\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+job_detail/\s\.html?ka=search_list_\d'), callback="parse_job", follow=False),
    )

    def parse_job(self, response):
        title = response.xpath("//div[@class='job-banner']//div[@class='name']/h1/text()").get().strip()
        salary = response.xpath("//div[@class='job-banner']//div[@class='name']/span/text()").get().strip()
        job_info = response.xpath("//div[@class='job-banner']//p//text()").getall()
        city = job_info[0]
        work_years = job_info[1]
        education = job_info[2]
        company = response.xpath("//div[@class='sider-company']//div[@class='company-info']/a[1]/@title").get().strip()
        item = BossItem(name=title, salary=salary, city=city, work_years=work_years, education=education,company=company)
        yield item
