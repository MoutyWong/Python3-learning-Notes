#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pdb

# exercises :递归函数移动汉诺塔
def move(n, a, b, c):
    if n == 1:
        print('Move2:', a, '--->', c)
        pdb.set_trace()
        return
    pdb.set_trace()
    move(n - 1, a, c, b)
    pdb.set_trace()
    print('Move1:', a, '--->', c)
    move(n - 1, b, a, c)
move(3, 'A', 'B', 'C')
