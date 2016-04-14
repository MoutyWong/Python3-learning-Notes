#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filter过滤函数 根据返回值是True或False决定去留
# example
def is_old(n):
    return n % 2 == 1
print(list(filter(is_old, [1, 2, 3, 4, 5, 6])))
print([n for n in [1, 2, 3, 4, 5, 6] if n % 2 == 1], '\n')
# example 把一个序列中的空字符删掉
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', 'B', ' ', 'C'])))
print([n for n in ['A', 'B', ' ', 'C'] if n and n.strip()], '\n')


# 用filter求素数
def prime():
    def _odd_iter():
        n = 1
        while True:
            n = n + 2
            yield n
    def _not_divisible(n):
        return lambda x: x % n > 0
    yield 2
    iList = _odd_iter()
    while True:
        n = next(iList)
        yield n
        iList = filter(_not_divisible, iList)
for n in prime():
    if n < 1000:
        print(n)
    else:
        break
        
# exercises 用filter筛选回数
def is_palindrome(n):
    return int(str(n)[::-1]) == n
    # nStr = str(n)
    # nlen = len(nStr)
    # i = nlen // 2
    # fooStr = nStr[::-1]
    # if nStr[:i] == fooStr[:i]:
    #     return True
    # else:
    #     return False
    
output = filter(is_palindrome, range(1, 1000))
print(list(output))
    