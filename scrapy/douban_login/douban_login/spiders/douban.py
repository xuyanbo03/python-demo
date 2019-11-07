# -*- coding: utf-8 -*-
import scrapy
from urllib import request
from PIL import Image
from base64 import b64encode
import requests


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/passport/login']
    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    profile_url = 'https://www.douban.com/people/610958401/'
    edifsignature_url = ''

    def parse(self, response):
        formdata = {
            'ck': '',
            'name': '610958401@qq.com',
            'password': 'xxx',
            'remember': 'true',
            'ticket': ''
        }
        captcha_url = response.css('img#captcha_image::attr(src)').get()
        if captcha_url:
            captcha = self.regonize_captcha(captcha_url)
            formdata['captcha-solution'] = captcha
            captcha_id = response.xpath("//input[@name='captcha-id']/@value").get()
            formdata['captcha-id'] = captcha_id
        yield scrapy.FormRequest(url=self.login_url, formdata=formdata, callback=self.parse_after_login)

    def parse_after_login(self, response):
        if response.url == 'https://www.douban.com':
            print("登录成功！")
            yield scrapy.Request(self.profile_url, callback=self.parse_profile)
        else:
            print("登录失败！")

    def parse_profile(self, response):
        print(response.url)
        if response.url == self.profile_url:
            print("进入个人中心")
            ck = response.xpath("//input[@name='ck']/@value").get()
            formdata = {
                'ck': ck,
                'signature': 'scrapy'
            }
            yield scrapy.FormRequest(url=self.edifsignature_url, formdata=formdata, callback=self.parse_none)
        else:
            print("没有进入个人中心")

    def parse_none(self, response):
        pass

    # def regonize_captcha(self, image_url):
    #     request.urlretrieve(image_url, 'captcha.png')
    #     image = Image.open('captcha.png')
    #     image.show()
    #     captcha = input("请输入验证码：")
    #     return captcha
    def regonize_captcha(self, image_url):
        catpcha_url = image_url
        request.urlretrieve(catpcha_url, 'captcha.png')
        recognize_url = ''

        formdata = {}
        with open('captcha.png', 'rb') as fp:
            data = fp.read()
            pic = b64encode(data)
            formdata['pic'] = pic

        appcode = ''
        headers = {
            'Content-Type': '',
            'Authorization': 'APPCODE ' + appcode
        }

        response = requests.post(recognize_url, data=formdata, headers=headers)
        result = response.json()
        code = result['result']['code']
        return code
