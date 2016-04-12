#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# exercises
height = 1.75
weight = 80.5
bmi = weight / height ** 2
if bmi < 18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 32:
    print('肥胖')
elif bmi > 32:
    print('严重肥胖')
