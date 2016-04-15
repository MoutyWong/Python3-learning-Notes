#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Anonymous function 匿名函数 lambda
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7])))

# 匿名函数只能有一个表达式，不用写return，返回值就是表达式的结果
# 匿名函数的好处就是不用担心函数名冲突
# 匿名函数也是一个函数对象，可以把匿名函数赋值给一个变量，再利用变量调用该函数
# example
f1 = lambda x: x * x
print(f1(5), '\n')

def build(x, y):
    return lambda: x * x + y ** 2
f2 = build(3, 5)
print(build(3, 5)(), '\n')

# Decorator 装饰器 函数对象有一个__name__属性，可以拿到函数的名字
print(f2.__name__, '\n')
def log(func):
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2016-4-15')
now()
print('now name:', now.__name__)

# 自定义log文本 要用到三层嵌套
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log2('execute')
def now2():
    print('2016-4-15 11:06')
now2()
print('now2 name:',now2.__name__)

# 完整代码
import functools 

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2016-4-15')
now()
print('now name:', now.__name__)

# 自定义log文本 要用到三层嵌套
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log2('execute')
def now2():
    print('2016-4-15 11:06')
now2()
print('now2 name:',now2.__name__, '\n')


# exercises
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call', func.__name__)
        tempF = func(*args, **kw)
        print('end call', func.__name__)
        return
    return wrapper

@logger
def test1():
    print('test ====')
test1()
print(test1.__name__, '\n')

# 
def logger2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(text, func.__name__)
            tempF = func(*args, **kw)
            print(text, func.__name__)
            return
        return wrapper
    return decorator
@logger2('kkkk')
def test2():
    print('test ==== 2')
test2()
print('test2 name:', test2.__name__)