#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 排序算法
# python 内置的sorted()函数可以对list排序, sorted() 也是高阶函数
print(sorted([23, 546, 12, 34, 8, 9, -23]))

# sorted()也是高阶函数，它可以接收一个key函数来实现自定义的排序， 
# example 按绝对值大小排序
print(sorted([345,23,3452,5634,-214,-436,2345,-9], key=abs)) 

# 字符串排序，忽略大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 要反向排序，只要再后传入第三个参数reverse = True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# exercises
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
print(sorted(L, key=by_name))

def by_score(t):
    return t[1]
print(sorted(L, key=by_score))
