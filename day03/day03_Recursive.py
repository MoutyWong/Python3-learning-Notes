#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 递归函数recursive function
def fact(n):
    if not isinstance(n, (int, float)):
        raise TypeError('bad operand type')
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(100))

# 尾递归
def fact2(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact2(10))
