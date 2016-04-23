#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# hashlib
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest(), '\n')

# SHA1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
print('\n')

# exercises
def calc_md5(pwd):
	pmd = hashlib.md5()
	pmd.update(pwd.encode('utf-8'))
	return pmd.hexdigest()

print('123456 ==>', calc_md5('123456'))
print('password ==>', calc_md5('password'))
print('888888 ==>', calc_md5('888888'))

db = {'michael': 'e10adc3949ba59abbe56e057f20f883e',
	'bob': '5f4dcc3b5aa765d61d8327deb882cf99',
	'alice': '21218cca77804d2ba1922c33e0151105'}

def login(user, pwd):
	pwd_md5 = hashlib.md5()
	pwd_md5.update(pwd.encode('utf-8'))
	if db[user] == pwd_md5.hexdigest():
		return True
	else:
		return False

print(login('michael', 'password'))
print(login('michael', '123456'))
print('\n')

regdb = {}

def register(username, password):
	pwd_md5 = hashlib.md5()
	pwd_md5.update((password + username + 'the-Salt').encode('utf-8'))
	regdb[username] = pwd_md5.hexdigest()

register('michael', '121212')
register('zhangsan', '121212')
register('lisi', '121212')
print(regdb)

def login(username, password):
	pwd_md5 = hashlib.md5()
	pwd_md5.update((password + username + 'the-Salt').encode('utf-8'))
	i = 0	
	for n in regdb:
		if username == n:
			i = 1
	if i:
		if regdb[username] == pwd_md5.hexdigest():
			print('Login Success!')
		else:
			print('password Wrong!')
	else:
		print('You don\'t exits!')

login('xiaoming','121212')
login('zhangsan','121212')


