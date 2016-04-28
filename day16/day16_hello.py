#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def application(environ, star_response):
	star_response('200 ok', [('Content-Type', 'text/html')])
	body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
	print(environ)
	return [body.encode('utf-8')]