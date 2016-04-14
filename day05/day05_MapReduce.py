#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 高阶函数
# map函数 参数一为一个函数，参数2为一个Iterable,return 一个Iterator
r = map(int, '123456')
print(list(r))

# reduce 把结果继续和序列的下一个元素累积计算，
# example
from functools import reduce
def add(x, y):
    return x * 10 + y
a =  reduce(add, [1, 2, 3, 4, 5, 6])
print(a)
# 自己写一个str2int函数
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}[s]
    return reduce(fn, map(char2num, s))
print(str2int('2233'), '\n')

# exercises 利用map()函数，把用户输入的不规范英文名字，变为首字母大写，其它小写的规范名字。
aList = ['adam', 'LISA', 'barT']
def str2up(list1):
    def up(s):
        return s.capitalize()
    return map(up, list1)
for x in str2up(aList):
    print(x)
print('\n')
# exercises 编写一个prod()函数，接受一个list利用reduce()求积
sList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def prod(s):
    def fnn(x, y):
        return x * y
    return reduce(fnn, s)
print(prod(sList), '\n')

# 利用map和reduce编写一个str2float函数，把字符串‘123.456’转换成浮点数123.456
def str2float(s):
    point = 0
    def fn(x, y):
        nonlocal point
        if y == -1:
            point = 1
            return x
        if point == 0:
            return x * 10 + y
        else:
            point = point * 10
            return x + y/point
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}[s] 
    return reduce(fn, map(char2num, s))
print(str2float('123.456'))