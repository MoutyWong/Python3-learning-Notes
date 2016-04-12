#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 字典dictionary

dic1 = {'Micheal': 95, 'Bob': 75, 'Tracy': 85}
print(dic1['Bob'])
dic1['Amor'] = 99
dic1['Mout'] = 100
print(dic1)

a = 'Amor' in dic1
print(a)

# set
s1 = set([1, 2, 3])
print(s1)
s1.add(5)
print(s1)
s1.remove(3)
print(s1)

s2 = set([1, 2, 7, 8])
print(s1 & s2)
print(s1 | s2)

l1 = ['d', 'e', 'a', 'c', 'b']
l1.sort()
print(l1)
str1 = 'abc'
str1.replace('a', 'A')
print(str1)
