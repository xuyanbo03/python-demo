# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymysql import cursors
from twisted.enterprise import adbapi


class JianshuSpiderPipeline(object):
    def __init__(self):
        dbparams = {
            'host': 'hadoop01',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'jianshu',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (str(item['origin_url']), str(item['article_id']), str(item['title']), str(item['author']), str(item['avatar']), item['pub_time'], int(item['word_count']),int(item['read_count']),int(item['like_count']),int(item['comment_count']), str(item['subjects']), str(item['content'])))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into article(id,origin_url,article_id,title,author,avatar,pub_time,word_count,read_count,like_count,comment_count,subjects,content) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql


class JianshuTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': 'hadoop01',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'jianshu',
            'charset': 'utf8',
            'cursorclass': cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into article(id,origin_url,article_id,title,author,avatar,pub_time,word_count,read_count,like_count,comment_count,subjects,content) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error, item, spider)
        return item

    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (str(item['origin_url']), str(item['article_id']), str(item['title']), str(item['author']), str(item['avatar']), item['pub_time'], int(item['word_count']),int(item['read_count']),int(item['like_count']),int(item['comment_count']), str(item['subjects']), str(item['content'])))

    def handle_error(self, error, item, spider):
        print(error)
