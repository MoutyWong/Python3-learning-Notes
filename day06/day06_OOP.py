#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Object Oriented Programmin
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 88)
bart.print_score()
lisa.print_score()

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两下划线__,在python中，实例变量名如果以__开关，就变成了一个私有变量private，只有内部可以访问，
class Student2(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
        
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
        
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')		
			
print('\n')

# 继承和多态
# Subclass 子类，被继承的class称为基类或超类(Base class, Super class)

# example
class Animal(object):
	def run(self):
		print('Animal is runing...')

# Dog 和 Cat继承于Animal
class Dog(Animal):

	def run(self):
		print('Dog is runing...')
		
	def eat(self):
		print('Eating meat...')
	
class Cat(Animal):
	
	def run(self):
		print('Cat is runing...')
		
dog = Dog()
dog.run()

cat = Cat()
cat.run()

print('\n')
# type()函数返回对象类型
print(type(123))
print(type(123) == type(345))
print(type(123) == int)
print(type('123') == type(123), '\n')

# 如果要判断一个对象是否是函数，可以用types模块中定义的常量
import types
def fn():
	pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinMethodType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)


print('\n')
# 获得一个对象的所有属性和方法可以用dir()函数,它返回一个包含字符串的list
# example
print(dir('123'), '\n')

# 自定义类，如果想用len(),要自己写一个__len__方法：
class MyDog(object):
	
	def __len__(self):
		return 10

ddog = MyDog()
print(len(ddog), '\n')

# getattr() setattr() hasattr()
# example
class MyObject(object):
	
	def __init__(self):
		self.x = 9
		
	def power(self):
		return self.x * self.x
		
obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
print(setattr(obj, 'y', 18))
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)

# 可以传入一个default参数,如果不存在，不返回默认值
print(getattr(obj, 'z', 404))
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fnn = getattr(obj, 'power')
print(fnn)
print(fnn())
