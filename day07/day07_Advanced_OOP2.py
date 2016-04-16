#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Mixin 多重继承
class Animal(object):
	pass
	
class Mammal(Animal):
	pass

class Bird(Animal):
	pass
	
class Dog(Mammal):
	pass
	
class Bat(Mammal):
	pass
	
class Parrot(Bird):
	pass
	
class Ostrich(Bird):
	pass
	
class Runnable(object):
	def run(self):
		print('%s Runing...' % self.__class__.__name__)

class Flyable(object):
	def fly(self):
		print('%s Flying...' % self.__class__.__name__)	
		
class Dog(Mammal, Runnable):
	pass
	
class Bat(Mammal, Flyable):
	pass
	
dog = Dog()
dog.run()
print('\n')

