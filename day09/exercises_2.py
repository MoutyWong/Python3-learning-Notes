#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' find files '

__author__ = 'Mouty Wong'

import os

pwd = os.path.abspath('.')
filename = input('Please enter your file:')
for root, dirs, files in os.walk(pwd):
	for name in files:
		if filename in name:
			print('文 件 名：', name)
			print('相对路径：', root.replace(pwd, '.'))