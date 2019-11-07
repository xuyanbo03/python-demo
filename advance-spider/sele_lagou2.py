#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 使用selenium方式模拟浏览器，通过xpath在获取数据,最后写入csv文件
from lxml import etree
import time
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv


class LagouSpider(object):
    driver_path = r'D:\tool\chromedriver\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_hadoop?labelWords=&fromSearch=true&suginput='
        self.positions = []
        fp = open('lagou.csv', 'a', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(fp, ['url', 'name', 'company_name', 'salary', 'city', 'work_years', 'education','desc'])
        self.writer.writeheader()

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            # 显示等待10s
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='pager_container']/span[last()]"))
            )
            self.parse_list_page(source)
            try:
                # 获取下一页按钮，如果没有下一页，程序终止
                next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
                if "pager_next_disabled" in next_btn.get_attribute("class"):
                    break
                else:
                    next_btn.click()
            except:
                print(source)
            time.sleep(1)

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)

    def request_detail_page(self, url):
        # self.driver.get(url)
        # 执行js脚本，打开新页面，并且切换driver到新页面，访问完关闭后，再切换回来
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='job-name']/h1[@class='name']"))
        )
        source = self.driver.page_source
        self.parse_detail_page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        position_name = html.xpath("//div[@class='job-name']/h1[@class='name']/text()")[0]
        job_requests_spans = html.xpath("//dd[@class='job_request']//span")
        salary = job_requests_spans[0].xpath(".//text()")[0].strip()
        city = job_requests_spans[1].xpath(".//text()")[0].strip()
        city = re.sub(r'[\s/]', '', city)
        work_years = job_requests_spans[2].xpath(".//text()")[0].strip()
        work_years = re.sub(r'[\s/]', '', work_years)
        education = job_requests_spans[3].xpath(".//text()")[0].strip()
        education = re.sub(r'[\s/]', '', education)
        desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
        desc = re.sub('(\xa0|•|【|】|\s)', '', desc)
        company_name = html.xpath("//em[@class='fl-cn']//text()")[0].strip()
        url = self.driver.current_url
        position = {
            'url': url,
            'name': position_name,
            'company_name': company_name,
            'salary': salary,
            'city': city,
            'work_years': work_years,
            'education': education,
            'desc': desc
        }
        self.writer.writerow(position)
        self.positions.append(position)
        print(position)
        print('=' * 50)


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()
