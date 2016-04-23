#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct

def check_bmp(file):
	with open(file, 'rb') as f:
		read = f.read()
		stt = struct.unpack('<ccIIIIIIHH', read[:30])
		if stt[0] == b'B' and stt[1] == b'M':
			print('This picture is BMP picture')
			print('This picture size:%s X %s' % (stt[6], stt[7]))
			print('Colors:', stt[9])
		else:
			print('This is no\'t BMP picture')
			
files = input('Please enter file name:')
check_bmp(files)