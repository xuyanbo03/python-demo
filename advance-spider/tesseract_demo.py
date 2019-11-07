#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'D:\tool\tesseract\Tesseract-OCR\tesseract.exe'

image = Image.open('a.jpg')
text = pytesseract.image_to_string(image, lang='chi_sim')
print(text)
