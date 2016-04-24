#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入socket库
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('192.168.2.104', 9999))
# s.send(b'hello')
while True:
	# send = input('Your say:')
	# s.send(send.encode('utf-8'))
	buffer = []
	while True:
		d = s.recv(1024)
		if d:
			buffer.append(d)
		else:
			data = b''.join(buffer)
			print('server:', data)
			break
	
# buffer = []
# while True:
# 	# 每次最多接收1k字节
# 	d = s.recv(1024)
# 	if d:
# 		buffer.append(d)
# 	else:
# 		break
# data = b''.join(buffer)
# # 关闭连接
# s.close()
# print(data.decode('utf-8'))
'''
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件
with open('sina.html', 'wb') as f:
	f.write(html)
'''