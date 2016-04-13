#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 列表------list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print('\n')
# 倒序
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
# 元素追加
classmates.append('Adam')
print(classmates)
# 追加到指定位置
classmates.insert(1,'Jack')
print(classmates)
# 删除元素---默认删除最后的元素
classmates.pop()
print(classmates)
# 删除指定位置元素
classmates.pop(1)
print(classmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Pull'
print(classmates)
# list里面的元素可以是不同类型的
l2 = ['Pull', 123, 123.456, ['asp', 'php']]
print(l2)
print(l2[3][1])
# 空列表
l3 = []
print(len(l3))
