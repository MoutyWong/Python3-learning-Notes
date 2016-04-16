#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Advanced Object-Oriented programming 面向对象高级编程
# 使用__slots__
class Student(object):
	__slots__ = ('name', 'age', 'score')
	
	def set_age(self, age):
		self.age = age

from types import MethodType
s = Student()
s.name = 'Michael'
print(s.name)
# s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)
print('\n')

# @property
# 在set_score()中检查参数
class Student2(object):
	
	# __slots__ = ('name', 'age', 'score')
	
	def get_score(self):
		return self._score
	
	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must be tween 0 ~ 100')	
		self._score = value
		
s2 = Student2()
s2.set_score(100)
print(s2.get_score(), '\n')
		
# property @property是一个装饰器decorator
class Student3(object):
	
	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be integer')
		if value < 0 or value > 100:
			raise ValueError('socre must be tween 0 ~ 100')	
		self._score = value
		
s3 = Student3()
s3.score = 99
print(s3.score)
		
# @property 可以设置只读属性，只定义getter方法，不定义setter方法就是一个只讲习属性
class Student4(object):
	
	@property
	def birth(self):
		return self._birth
		
	@birth.setter
	def birth(self, value):
		self._birth = value
	
	@property
	def age(self):
		return 2015 - self._birth

s4 = Student4()
s4.birth = 1992
print(s4.age, '\n')

# exercises 利用@property给一个Screen对象加上width 和height 属性，以及一个只读属性resolution
class Screen(object):
	
	@property
	def width(self):
		return self._width
		
	@width.setter
	def width(self, value):
		if not isinstance(value, int):
			raise ValueError('width must be integer')
		if value < 0:
			raise ValueError('value must be greater than zero')
		self._width = value
		
	@property
	def hight(self):
		return self._hight
		
	@hight.setter
	def hight(self, value):
		if not isinstance(value, int):
			raise ValueError('hight must be integer')
		if value < 0:
			raise ValueError('hight must be greater than zero')
		self._hight = value
	
	@property
	def resolution(self):
		return self._width * self._hight

screen = Screen()
screen.width = 1920
screen.hight = 1080
print(screen.resolution)