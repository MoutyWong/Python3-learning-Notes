#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定制类
class Student(object):
	def __init__(self, name):
		self.name = name
		
print(Student('Michael'), '\n')

# 定义 __str__()方法，返回字符串
class Student2(object):
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return 'Student2 object (name: %s)' % self.name
	# __repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
	__repr__ = __str__
	
print(Student2('Michael'), '\n')

# __iter__ 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# example 斐波那契数列
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1
		
	def __iter__(self):
		return self
		
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100000:
			raise StopIteration();
		return self.a
	
for n in Fib():
	print(n)

# 要像list那样按照下标取出元素，需要实现__getitem__()方法
class Fibn(object):
	def __getitem__(self, n):
		a, b  = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a
		
print(Fibn()[10])

# slice 切片对象。 
class Fibnq(object):
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b  = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b  = 1, 1
			aList = []
			for x in range(stop):
				if x >= start:
					aList.append(a)
				a, b = b, a + b
			return aList
			
print(Fibnq()[:10], '\n')

# __getattr__  动态返回属性，只有在没有找到属性的情况下，对调用__getattr__，
class Student3(object):
	def __init__(self):
		self.name = 'Michael'
	
	def __getattr__(self, attr):
		if attr == 'score':
			return 100
		# 返回函数
		if attr == 'age':
			return lambda: 25
		raise AttributeError('\'Student3\' object has no attribute \'%s\'' % attr)
		
print(Student3().score)
print('\n')

# 利用完全动态的__getattr__，写一个链式调用
class Chain(object):
	def __init__(self, path = ''):
		self._path = path
	
	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))
		
	def __str__(self):
		return self._path
		
	__repr__ = __str__
	
print(Chain().status.user.timeline.list)

class GitChain(object):
	def __init__(self, path = 'GET '):
		self._path = path
		
	def users(self, path):
		return GitChain('%s/users/:%s' % (self._path, path))	
	
	def __getattr__(self, path):
		return GitChain('%s/%s' % (self._path, path))
	
	def __str__(self):
		return self._path
		
print(GitChain().users('Michael').repos)

print('\n')
# __call__ 
class Human(object):
	def __init__(self, name):
		self.name = name
		
	def __call__(self):
		print('My name is %s.' % self.name)
		
print(Human('Michael')())
print('\n')
# 判断一个对象能不能被调用，能被调用的就是Callable对象
print(callable(max))
print(callable(Student))
print(callable(Human))
print(callable([1, 2, 3, 4]))
print(callable(None))