#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' test multiprocessing '

__author__ = 'Leslie Wong'

# multiprocessing 多进程
import os

from multiprocessing import Process
'''
# Unix/Linux fork()调用多进程
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac
pid1 = os.fork()
print('pid1 : ', pid1)
if pid1 == 0:
	print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
	print('I (%s) just created a child process (%s)' % (os.getpid(), pid1))
print('\n')
'''
# multiprocessing 跨平台版本的多进程模块
# multiprocessing模块提供了一个Process类来代表一个进程对象

# 子进程要执行的代码
def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target=run_proc, args=('test',))
	print('Child process will start.')
	p.start()
	p.join()
	print('Child process end.')
	
	
	