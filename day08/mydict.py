#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a Dict calss '

__author__ = 'Leslie Wong'

# Unit test 单元测试是用来对一个模块，一个函数或者一个类来进行正确性检验的测试工作
# exercises
class Dict(dict):
	
	def __init__(self, **kw):
		super().__init__(**kw)
	
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
			
	def __setattr__(self, key, value):
		self[key] = value
			
# d = Dict(a = 1, b = 2)
# print(d.a)
# print(d['b'])


