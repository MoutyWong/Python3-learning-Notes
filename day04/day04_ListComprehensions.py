#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式 list comprehensions

# example 生成list[1, 2, ..., 10]
aList = list(range(1, 11))
print(aList)
# 生成['1 X 1',..., '10 X 10']，用循环太繁琐
List2 = []
for x in range(1, 11):
    List2.append('%d X %d' % (x, x))
print(List2)
print('\n')
# 列表生成式，要用[] 括起来
List3 = [x * x for x in range(1, 10)]
print(List3)
# for...in后面可带判断
List3 = [x * x for x in range(1, 10) if x % 2 == 0]
print(List3, '\n')

# 可以使用两层循环，可以生成全排列
List4 = [m + n + x for m in 'ABC' for n in '123' for x in 'XYZ' if (m + n + x)[0] != 'A']
print(List4, '\n')

# 运用列表生成式，列出当前目录下的所有文件和目录名，
import os # 导入os模块，
DirectoryList = [d for d in os.listdir('.')]
print(DirectoryList, '\n')

# 把一个list中所有的字符串变成小写
sList = ['Hello', 'World', 'IBM', 'Apple']
sList = [s.lower() for s in sList]
print(sList, '\n')

# exercises
eList = ['Hello', 'World', 18, 'Apple', None]
eList2= [x.lower() + ' = ' + x.upper() for x in eList if isinstance(x, (str))]
print(eList2)
