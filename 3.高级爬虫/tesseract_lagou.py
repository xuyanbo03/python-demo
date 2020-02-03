#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pytesseract
from PIL import Image
from urllib import request
import time


def captcha():
    pytesseract.pytesseract.tesseract_cmd = r'D:\tool\tesseract\Tesseract-OCR\tesseract.exe'
    url = ''
    while True:
        request.urlretrieve(url, 'captcha.png')
        image = Image.open('captcha.png')
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(3)


if __name__ == '__main__':
    captcha()
