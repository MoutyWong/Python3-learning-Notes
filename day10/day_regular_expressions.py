#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

s = re.match(r'^\d{3}\-\d{3,8}$', '010-123456')
print(s)

s2 = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
print(s2)

if s2:
	print('ok')
else:
	print('failed.')
print('\n')

# 切分字符串
print('a b  c'.split(' '))
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\@\.]', 'abc@gmail.com'))
print(re.split(r'[\,\s]+', 'a,b,c,,d e  f'))
print('\n')

# 分组
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组(Group)
s3 = re.match(r'^(\d{3})\-(\d{3,8})$', '010-1233134')
print('%s, %s, %s, %s' % (s3, s3.group(), s3.group(1), s3.group(2)))
s4 = re.match(r'^([\w\d\_]+)\@([\w\d]+)\.(\w+)$', '4asdf4@gmail.com')
print(s4.groups())
t = '23:05:36'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups(), '\n')

# 贪婪匹配
print(re.match(r'^(\d+)(0*)$', '1023400000').groups())
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
print(re.match(r'^(\d+?)(0*)$', '1023400000').groups())
print('\n')

# 编译  编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
re_telepthone = re.compile(r'^(\d{3})\-(\d{3,8})$')
# 使用
print(re_telepthone.match('020-3422234').groups())

print('\n')

# exercises
re_email = re.compile(r'^([\d\w\_]+)\@([\d\w]+)\.(\w+)$')
re_nameemail = re.compile(r'^\<([\d\w\s]+)\>\s([\w\_]+)\@([\d\w]+)\.(\w+)$')
print(re_email.match('mouty216@gmail.com').groups())
print(re_nameemail.match('<Tom Paris> Tom@voyager.org').groups())
