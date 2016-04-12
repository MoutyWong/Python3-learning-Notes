#!/usr/bin/env python7
# -*- coding:utf-8 -*-

# 自定义函数 defined
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >=0:
        return x
    else:
        return -x
print(my_abs(-22))

# 导入包
import math

# 返回多值函数  实际上是返回一个tuple！ 但是，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，python的函数返回多值其实就是一个tuple，但是写起来更方便。
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi /6)
r = move(100, 100, 60, math.pi /6)
print(x, y, r)
