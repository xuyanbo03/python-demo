#!/usr/bin/python3
# -*- coding:utf-8 -*-
import threading

VALUE = 0
gLock = threading.Lock()

# 加锁机制
def add_val():
    global VALUE
    gLock.acquire()
    for x in range(1000000):
        VALUE += 1
    gLock.release()
    print(VALUE)


if __name__ == '__main__':
    for x in range(2):
        t = threading.Thread(target=add_val)
        t.start()
