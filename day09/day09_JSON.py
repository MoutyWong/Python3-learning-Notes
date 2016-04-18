#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JSON 
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
# JSON表示的对象就是标准的JavaScript语言的对象

# python 对象变成JSON

import json
import os

d = dict(name = 'Bob', age = 20, score = 99)
print(json.dumps(d))

# json.dumps()方法返回一个str，内容就是标准的JSON，json.dump()方法可以直接把JSON写入一个file-like Object
if 'dump.json' not in os.listdir('.'):
	os.mknod('dump.json')
f = open('dump.json', 'w')
json.dump(d, f)
f.close()



# JSON反序列化为Python对象，用loads()或者load()立法
json_str = json.dumps(d)
d2 = json.loads(json_str)
print(d2)

os.remove('dump.json')


# JSON 进阶

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

def student2dict(std):
	return {'name': std.name, 'age': std.age, 'score': std.score}

stu = Student('Michael', 18, 99)
jstr = json.dumps(stu, default=student2dict)
print(jstr)

# 把任意Class的实例变为dict
print(json.dumps(stu, default=lambda obj: obj.__dict__))

# JSON反序列化为一个Class对象实例
def dict2studen(dic):
	return Student(dic['name'], dic['age'], dic['score'])

jdic = json.loads(jstr)
stu2 = dict2studen(jdic)
print(stu2)
