#!/usr/bin/python3
# -*- coding:utf-8 -*-
import threading
import time
from queue import Queue


# Queue线程安全队列demo

def set_val(q):
    i = 0
    while True:
        q.put(i)
        i += 1
        time.sleep(1)


def get_val(q):
    while True:
        print(q.get(q))


if __name__ == '__main__':
    q = Queue(4)
    t1 = threading.Thread(target=set_val, args=[q])
    t2 = threading.Thread(target=get_val, args=[q])
    t1.start()
    t2.start()
