#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# exercises ax**2 + bx + c = 0
import math

def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(b, (int ,float)):
        raise TypeError('bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    if a != 0:
        if b != 0:
            x1 = ((-b) - math.sqrt(b*b - 4*a*c)) / (2 * a)
            x2 = ((-b) + math.sqrt(b*b - 4*a*c)) / (2 * a)
            return x1, x2
    else:
        x = (-c) / b
        return x
r = quadratic(2, 3, 1)
print(r)
r = quadratic(1, 3, -4)
print(r)
r = quadratic(0, 3, -4)
print(r)
