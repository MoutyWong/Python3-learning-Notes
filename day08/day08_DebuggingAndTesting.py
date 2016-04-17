#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Debugging
# Python 内置了一套异常处理机制，来帮助我们进行错误处理
# Python的pdb可以让我们以单步方式执行代码

# try...except...finally
try:
	print('try...')
	r = 10 / 0
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
finally:
	print('finally...')
print('END\n')

try:
	print('try...')
	r = 10 / int('a')
	print('result:', r)
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:', e)
else:
	print('no error!')
finally:
	print('finally...')
print('END\n')

# Python的错误也是class，所有的错误都继承自BaseException

def foo(s):
	return 10 /int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar('0')
	except Exception as e:
		print('Error:', e)
	else:
		print('No Error!')
	finally:
		print('finally...')
main()
print('\n')

# Python 内置的logging模块可以非常容易地记录错误信息
import logging
def fn(s):
	return 10 / int(s)
	
def bar(s):
	return fn(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
main()
print('==end==\n')

# 断言 assert
def fnn(s):
	n = int(s)
	assert n != 0, 'n is zero'
	return 10 / n
fnn('0')
print('------end-----\n')