#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器generator
# 创建generator方法一，把[]改成()
List1 = [x * x for x in range(10)]
print(List1, '\n')
# 把[]改成()
Gener1 = (x *x for x in range(10))
print(Gener1, '\n')
# 打印generator可以用next()
print(next(Gener1), '\n')
for n in Gener1:
    print(n)
print('\n')
# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    fibList = []
    while n < max:
        # print(b)
        fibList.append(b)
        a, b = b, a +b
        n += 1
    fibList.append('done')
    return fibList
print(fib(10), '\n')

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n +1
    return 'done'
fList = fib2(10)
print(fList, '\n')

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib2(6)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 杨辉三角
def pas_triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

if __name__ == "__main__":
    g = pas_triangles()
    for n in range(10):
        print(next(g))
