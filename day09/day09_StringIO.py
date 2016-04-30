#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Input Output '

__author__ = 'Leslie Wong'

# StringIO 在内存中读写str
# 要把str写入StringIO，需要先创建一个StringIO，然后像文件一样写入
from io import StringIO
f = StringIO()
print(f.write('Hello'))
print(f.write(' '))
print(f.write('World'))
print(f.getvalue())
print('\n')
# getvalue()用于获取写入后的str


# 要读取StringIO，可以用一个str初始化StringIO，
f2 = StringIO('Hello!\nHi\nGoodbye!')
while True:
	s = f2.readline()
	if s == '':
		break
	print(s.strip())
print('\n')


# BytesIO 
# StringIO 只能操作str，如果要操作二进制数据，就需要使用BytesIO，BytesIO实现了在内存中读写bytes
from io import BytesIO
fb = BytesIO()
print(fb.write('中文'.encode('utf-8')))
print(fb.getvalue())

fb2 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(fb2.read())
print('\n')

# 操作文件和目录
import os
print(os.name) # 操作系统类型
# 如果是posix 说明系统是Linux, Unix, Mac OS X,如果是nt，就是windows系统
# uname() 获取详细系统信息
print(os.uname(),'\n')

# 环境变量 在操作系统中定义的环境变量，全部保存在os.environ
print(os.environ, '\n')
# 要获取某个环境变量可以调用os.environ.get('key')
print(os.environ.get('SHELL'), '\n')

# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录,首先把新目录的完整路径表示出来,然后创建一个目录
print(os.path.join('home/mouty/下载', 'testdir'))
os.mkdir('/home/mouty/下载/testdir')
# 删除一个目录
os.rmdir('/home/mouty/下载/testdir')

# os.path.split()可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('/home/mouty/下载/Git教程.pdf'))
# os.path.splitext() 可以直接让你得到文件扩展名。
print(os.path.splitext('/path/to/file.txt'))
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
# 文件操作，要求文件和目录真实存在
'''
# 文件重命名
os.rename('test.txt', 'test.py')
# 删除文件
os.remove('test.py')
'''
# 复制文件的函数在os模块中不存在，原因是复制文件并非由操作系统调用
# 复制文件可以用shutil模块copyfile()函数。

# 列出当前目录下所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出当前目录下所有的.py文件。
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']