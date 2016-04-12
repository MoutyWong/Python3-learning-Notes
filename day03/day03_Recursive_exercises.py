#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# exercises :递归函数移动汉诺塔
def move(n, a, b, c):
    if n == 1:
        print('Move2:', a, '--->', c)
        return
    move(n - 1, a, c, b)
    print('Move1:', a, '--->', c)
    move(n - 1, b, a, c)
move(2, 'A', 'B', 'C')
