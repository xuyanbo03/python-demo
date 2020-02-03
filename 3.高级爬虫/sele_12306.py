#!/usr/bin/python3
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Qiangpiao(object):
    driver_path = r'D:\tool\chromedriver\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Qiangpiao.driver_path)
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self.initmy_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.search_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
        self.passenger_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'

    def wait_input(self):
        self.from_station = input("出发地：")
        self.to_station = input("目的地：")
        # 出发时间格式为：yyyy-mm-dd
        self.depart_time = input("出发时间：")
        self.passengers = input("乘客姓名（如有多个乘客，用英文逗号隔开）：").split(',')
        self.trains = input("车次（如有多个车次，用英文逗号隔开）：").split(',')

    def _login(self):
        self.driver.get(self.login_url)
        WebDriverWait(driver=self.driver, timeout=1000).until(
            EC.url_to_be(self.initmy_url)
        )
        print('登录成功！')

    def _order_ticket(self):
        self.driver.get(self.search_url)
        # 等待出发地，目的地，出发时间正确
        WebDriverWait(driver=self.driver, timeout=1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'fromStationText'), self.from_station)
        )
        WebDriverWait(driver=self.driver, timeout=1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'toStationText'), self.to_station)
        )
        WebDriverWait(driver=self.driver, timeout=1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'train_date'), self.depart_time)
        )

        # 等待查询按钮可点击，如果可用，执行点击
        WebDriverWait(driver=self.driver, timeout=1000).until(
            EC.element_to_be_clickable((By.ID, 'query_ticket'))
        )
        searchBtn = self.driver.find_element_by_id('query_ticket')
        searchBtn.click()

        # 等待车次显示，遍历车次是否在trains中，点击预订
        WebDriverWait(driver=self.driver, timeout=1000).until(
            EC.presence_of_element_located((By.XPATH, ".//tbody[@id='queryLeftTable']/tr"))
        )
        tr_list = self.driver.find_elements_by_xpath(".//tbody[@id='queryLeftTable']/tr[not(@datatran)]")
        for tr in tr_list:
            train_number = tr.find_element_by_class_name("number").text
            if train_number in self.trains:
                left_ticket = tr.find_element_by_xpath(".//td[4]").text
                if left_ticket == "有" or left_ticket.isdigit:
                    print(train_number + "有票")
                    orderBtn = tr.find_element_by_class_name("btn72")
                    orderBtn.click()

                    # 等待来到确认乘客页面，点击提交
                    WebDriverWait(driver=self.driver, timeout=1000).until(
                        EC.url_to_be(self.passenger_url)
                    )
                    self.driver.implicitly_wait(10)
                    passengerBtn = self.driver.find_element_by_xpath("//ul[@id='normal_passenger_id']//input[@id='normalPassenger_0']")
                    passengerBtn.click()
                    submitBtn = self.driver.find_element_by_xpath("//div[@class='lay-btn']/a[@id='submitOrder_id']")
                    submitBtn.click()
                    confirmBtn = self.driver.find_element_by_xpath("//div[@id='confirmDiv']/a[@id='qr_submit_id']")
                    print(confirmBtn)

    def run(self):
        self.wait_input()
        self._login()
        self._order_ticket()


if __name__ == '__main__':
    spider = Qiangpiao()
    spider.run()
