#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 条件判断
age = 20
if age >= 18:
    print('Your age is:', age)
    print('adult')
else:
    print('Your age is:', age)
    print('teenager')

# elif
age2 = 18
if age2 >= 18:
    print('adult')
elif age2 >=6:
    print('teenager')
elif age2 < 6:
    print('kid')

# input
birth = input('birth: ')
if int(birth) < 2000:
    print('00前')
else:
    print('00后')
