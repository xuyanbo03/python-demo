#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time
import threading
import random

# Condition版生产者和消费者问题
gMoney = 1000
gCondition = threading.Condition()
gTimes = 0
gTotalTimes = 10


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100, 1000)
            gCondition.acquire()
            if gTimes >= gTotalTimes:
                gCondition.release()
                break
            gMoney += money
            gTimes += 1
            print('%s生产者了%d，还有%d' % (threading.current_thread(), money, gMoney))
            gCondition.notify_all()
            gCondition.release()
            time.sleep(1)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            gCondition.acquire()
            while gMoney <= money:
                if gTimes >= gTotalTimes:
                    gCondition.release()
                    return
                print('%s消费者消费%d，还有%d,不足' % (threading.current_thread(), money, gMoney))
                gCondition.wait()

            gMoney -= money
            print('%s消费者消费了%d，还有%d' % (threading.current_thread(), money, gMoney))
            gCondition.release()
            time.sleep(1)


if __name__ == '__main__':
    for x in range(3):
        t = Consumer(name='消费者%d' % x)
        t.start()
    for x in range(5):
        t = Producer(name='生产者%d' % x)
        t.start()
