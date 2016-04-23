#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# base64
import base64
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
a = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(a)
b = base64.urlsafe_b64encode(b'i\xb7\x1d\xfd\xef\xff')
print(b)
c = base64.urlsafe_b64decode('abcd--__')
print(c)

# exercises
def safe_base64_decode(s):
	if isinstance(s, bytes):
		s = s.decode()
	n = len(s) % 4
	s = s + '=' * n
	return base64.b64decode(s)

print(safe_base64_decode(b'YWJjZA'))
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode(b'YWJjZA')
# print(a)
