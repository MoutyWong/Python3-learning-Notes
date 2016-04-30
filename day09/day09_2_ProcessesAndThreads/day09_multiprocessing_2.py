#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Pool '

__author__ = 'Leslie Wong'


import os, time, random
from multiprocessing import Pool

# Pool进程池
# Pool 如果要启动大量的子进程，可以用进程池的方式批量创建子进程

def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))
	
if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4) # 限制同时执行进程数
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocess done...')
	p.close()
	p.join()
	print('All subprocess done.')
# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。