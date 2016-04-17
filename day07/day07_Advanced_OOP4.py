#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 枚举类 Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
# value属性则是自动赋给成员的int常量，默认从1开始计数
for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)
print('\n')

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
	
# @unique装饰器可以帮助我们检查保证没有重复值。
# 访问这些枚举类型可以有若干种方法：
day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(Weekday(1))
print(day1 == Weekday(1))

print('\n')

# 使用元类
# type() 可以查看一个类型或变量的类型，

class Hello(object):
	def hello(self, name = 'Michael'):
		print('hello', name)
		
h = Hello()
h.hello()
print(type(Hello))
print(type(h))
print('\n')

# 用type()动态生成class
# 要创建一个class对象，type()函数依次传入3个参数：
# 
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
def fn(self, name = 'World'):
	print('Hello', name)
	
Hi = type('Hi', (object,), dict(hello = fn))
hi = Hi()
hi.hello()
print(type(Hi))
print(type(hi))
print('\n')

# metaclass 元类
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)
		
class MyList(list, metaclass = ListMetaclass):
	pass
	
	