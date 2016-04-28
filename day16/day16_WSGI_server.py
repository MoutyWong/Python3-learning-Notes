#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 运行WSGI服务
# 导入wsgiref模块
from wsgiref.simple_server import make_server

from day16_hello import application

# 创建一个服务器，IP地址为空，端口是8000,处理函数是application
httpd = make_server('', 8000, application)
print('Serving HTTP on prot 8000...')

# 开始监听HTTP请求
httpd.serve_forever()