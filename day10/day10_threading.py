#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test threading '

__author__ = 'Leslie Wong'

# 多线程 python 的标准库提供了两个模块：_thread 和 threading，_thread是低级模块，threading是高级模块,对_thread进行了封装

import time, threading

# 新线程的代码
def loop():
	print('thread %s is runing...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)
	
print('thread %s is runing...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopTread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)