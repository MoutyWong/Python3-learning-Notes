#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable

# iteration
# python中迭代是通过for...in来完成的，
str1 = 'Michael'
for n in str1:
    print(n)
print('\n')

# dict 默认迭代的是key
dict1 = {'a': 1, 'b': 2, 'c': 3}
for key in dict1:
    print(key)
    # print(dict1[key])
for value in dict1.values():
    print(value)
for k, v in dict1.items():
    print(k, v)
for r in dict1.items():
    print(r)

# 判断是否可迭代的方法是通过collections 模块的Iterable类型判断
# str是否可迭代
print(isinstance('Michael', Iterable))
# list是否 可迭代
print(isinstance([1, 2, 3], Iterable))
# 整数是否可迭代
print(isinstance(123, Iterable))

# python的下标循环，通过python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(str1):
    print(i, value)
for i, value in enumerate(['a', 'b', 'c']):
    print(i ,value)

for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)
