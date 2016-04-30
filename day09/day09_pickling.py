#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' pickling '

__author__ = 'Leslie Wong'

# 序列化：我们把变量从内存中变成可存储或传输的过程称之为序列化 在python中叫pickling,的其他语言中也被称之为serialization, marshalling, flattening
# 反序列化：把变量内容从序列化的对象重新读到内存里称之为反序列化，unpickling

# python提供了pickle模块来实现序列化
# example
import pickle
import os

d = dict(name = 'Bob', age = 20, score = 88)
print(pickle.dumps(d), '\n')
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
# pickle.dump()可以直接把对象序列化后写入一个file-like Object
if 'dump.txt' not in os.listdir('.'):
	os.mknod('dump.txt')
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f2 = open('dump.txt', 'rb')
d2 = pickle.load(f2)
print(d2)
f2.close()

os.remove('dump.txt')