# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleSpiderItem(scrapy.Item):
    origin_url = scrapy.Field()
    article_id = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    avatar = scrapy.Field()
    pub_time = scrapy.Field()
    word_count = scrapy.Field()
    read_count = scrapy.Field()
    like_count = scrapy.Field()
    comment_count = scrapy.Field()
    subjects = scrapy.Field()
    content = scrapy.Field()

