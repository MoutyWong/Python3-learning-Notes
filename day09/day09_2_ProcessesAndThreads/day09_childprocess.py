#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' child process '

__author__ = 'Leslie Wong'

import os, subprocess, time, random
from multiprocessing import Process, pool, Queue

# subprocess 模块可以让我们非常方便地启动一个子进程，然后控制其输入输出

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r, '\n')

def fn():
	print('$ nslookup')
	p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
	print(output.decode('utf-8'))
	print('Exit code:', p.returncode)
fn()
