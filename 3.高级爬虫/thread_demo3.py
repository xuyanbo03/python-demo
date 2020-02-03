#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time
import threading
import random

# Lock版生产者和消费者问题
gMoney = 0
gLock = threading.Lock()
gTimes = 0
gTotalTimes = 10


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            if gTimes >= gTotalTimes:
                gLock.release()
                break
            gMoney += money
            gTimes += 1
            print('%s生产者了%d，还有%d' % (threading.current_thread(), money, gMoney))
            gLock.release()
            time.sleep(1)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 500)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print('%s消费者消费了%d，还有%d' % (threading.current_thread(), money, gMoney))
            elif gTimes >= gTotalTimes:
                gLock.release()
                break
            else:
                print('%s消费者消费%d，还有%d,不足' % (threading.current_thread(), money, gMoney))
            gLock.release()
            time.sleep(1)


if __name__ == '__main__':
    for x in range(5):
        t = Producer(name='生产者%d' % x)
        t.start()
    for x in range(3):
        t = Consumer(name='消费者%d' % x)
        t.start()
