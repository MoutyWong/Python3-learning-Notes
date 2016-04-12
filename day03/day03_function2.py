#!/usr/bin/env python3
# -*-coding:utf-8 -*-


# 设置默认参数
def power(x, n = 2):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(n, (int, float)):
        raise TypeError('bad operand type')
    sum = 1
    while n > 0:
        n -= 1
        sum = sum * x
    return sum
print(power(3))


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc())

# *nums 表示把 numms 这个list 的所有元素作为可变参数传进去，这种写法相当有用，而且很常见。
nums = [1, 2, 3, 4, 5, 6]
print(calc(*nums))

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 18)
person('Amor', 23, city = 'Wuxue')
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('jack', 24, **extra)

# 命名关键字参数
def person2(name, age, **kw):
    if 'city' in kw:
        print('有city参数')
    if 'job' in kw:
        print('有job参数')
    print('name:', name, 'age:', age, 'other', kw)
person2('Michael', 33, city = 'Beijing', job = 'Enginer')
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，会报错
def person3(name, age, *, city = 'Beijing', job):
    print(name, age, city, job)
person3('Bob', 24, city = 'Beijing', job = 'Enginer')
