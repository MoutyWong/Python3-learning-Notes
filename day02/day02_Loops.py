#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# for in 循环
names = ['Micheal', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for abs in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + abs
print(sum)
print(list(range(5)))
sum2 = 0
for x in range(101):
    sum2 = sum2 + x
print(sum2)

# while 循环
sum3 = 0
n = 99
while n > 0:
    sum3 = sum3 + n
    n -= 2
print(sum3)

l1 = ['Bart', 'Lisa', 'Adam', 'Micheal']
for name in l1:
    print('Hello, ',name)

i = 0
while 1:
    i += 1
    print(i)
