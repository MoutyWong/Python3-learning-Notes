#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Partial function偏函数
# int()函数默认按十进制转换

print(int('12345', base = 8))
print(int('1000000 \n', base = 2))

# functools.partial用来创建偏函数
import functools
int2 = functools.partial(int, base = 2)
print(int2('101010011001'))
