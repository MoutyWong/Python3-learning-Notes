#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 函数 function
# 求绝对值函数
print(abs(100))
print(abs(-100))

# 返回最大值和最小值函数====可接收多个参数
print(max(1,5,8))
print(min(23,55,72452,2314))

 # 数据类型转换
print('字符串转整型:', int('123'))
print('浮点型转整型:', int(12.34))
print('字符串转浮点:', float('12.34'))
print('数字转字符串:', str(123.4))
print('数字转字符串:', str(100))
print('数字转布尔型:', bool(1))
print('字符串转布尔:', bool(''))

# 函数别名
a = abs
print(a(-1))

# 十进制转十六进制
print(hex(100))

from day03_defined import my_abs
print(my_abs(-333))
