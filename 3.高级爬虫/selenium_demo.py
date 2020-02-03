#!/usr/bin/python3
# -*- coding:utf-8 -*-
from selenium import webdriver

driver_path = r'D:\tool\chromedriver\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://113.86.151.190:8118")
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
driver.get('https://www.ipip.net/ip.html')
# print(driver.page_source)
