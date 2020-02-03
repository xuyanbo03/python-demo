#!/usr/bin/python3
# -*- coding:utf-8 -*-
from time import sleep
import threading


def coding():
    for x in range(3):
        print('code %s' % threading.current_thread())
        sleep(1)


def drawing():
    for x in range(3):
        print('draw %s' % threading.current_thread())
        sleep(1)


# 传统的方式
def single_thread():
    coding()
    drawing()


# 多线程方式--函数
def multi_thread1():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)
    t1.start()
    t2.start()
    print(threading.enumerate())


class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('code %s' % threading.current_thread())
            sleep(1)


class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('draw %s' % threading.current_thread())
            sleep(1)


# 多线程方式--继承类
def multi_thread2():
    t1 = CodingThread()
    t2 = DrawingThread()
    t1.start()
    t2.start()
    print(threading.enumerate())


if __name__ == '__main__':
    # single_thread()
    # multi_thread1()
    multi_thread2()
