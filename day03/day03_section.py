#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 循环输出100以内的奇数
i = 0
while i < 100:
    if i % 2 != 0:
        print(i)
    i += 1

# 切片section
aList = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(aList[:3])

bList = list(range(100))
print(bList[-10:-4])
