#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# python中的另一种序列表 元组 tuple
# 元组tuple用双括号区分
# 元组为只读序列
classmates = ('Michel', 'Bob', 'Tarcy')
print(classmates)
# 只有一个元素的元组
t1 = (1,)
print(t1)
# '可变元组'
t2 = (1, 2, ['Amor', 'Mouty'])
print(t2)
t2[2][0] = '张梦弦'
t2[2][1] = '黄茂庭'
print(t2)

# exercises
l3 = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Pthon', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print('exercises 1:%s' % l3[0][0])
print('exercises 2:%s' % l3[1][1])
print('exercises 3:%s' % l3[2][2])
