#!/usr/bin/env python3
# -*- coding:utf-8 -*-
str = '\u4e2d\u6587'
print(str)
#
x = b'ABC'
print(x)

# 指定类型字符转换为字节码=============
e = 'ABC'.encode('ascii')
print(e)

z = '张三'.encode('utf-8')
print(z)
print('张三'.encode('gb2312'))

print ('===============')
# 字节码转换为指定类型字符=============
print(e.decode('ascii'))
print(z.decode('utf-8'))
# 格式化字符串
print('Hello, %s' % 'world')
print('%s, %s' % (x.decode('ascii'),z.decode('utf-8')))


# exercises
count1 = 72
count2 = 85
print('小明成绩提升百分点是 %.1f%%' % (count1 / (count2 - count1)))
