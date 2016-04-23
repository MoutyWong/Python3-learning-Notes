#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# itertools 提供了非常有用的用于操作迭代对象的函数
# 无限迭代器
import itertools
natuals = itertools.count(1)
for n in natuals:
	print(n)
	if n == 100000:
		break
		
# count()会创建一个无限的迭代器

# cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle('ABC')
i = 0
for c in cs:
	print(c)
	i += 1
	if i == 10000:
		break
		
# repeat() 负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('a', 10)
for n in ns:
	print(n)

# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个年代对象，它不会把无限个元素生成出来，事实上也不可能在内存中创建无限个元素

# 无限元素序列虽然可以无限迭代下去，但是通常我们会通过 takewhile() 等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# 迭代器操作函数
# chain()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBBCCAAAADADD'):
	print(key, list(group))
	
# 忽略大小写
for key, group in itertools.groupby('AABBAAaCcCCDDd', lambda c: c.upper()):
	print(key, list(group))
