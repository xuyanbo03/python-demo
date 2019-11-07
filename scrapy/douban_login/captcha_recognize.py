#!/usr/bin/python3
# -*- coding:utf-8 -*-
from urllib import request
from base64 import b64encode
import requests

catpcha_url = ''
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
print(code)
