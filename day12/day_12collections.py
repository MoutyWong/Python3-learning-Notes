#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# collections

# namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, tuple))

# deque
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
print(q, '\n')

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出keyError如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print(dd['key1'], dd['key2'], '\n') #key1,存在，key2不存在

# Orderedict Orderedict的key会按照插入的顺序排列，不是key本身排序
from collections import OrderedDict
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()), list(od.values()))
# orderedict 可以实现一个FIFO的dict，当容量超出限制时，先删除最早添加的key
class LastUpdatedOrdereDict(OrderedDict):
	
	def __init__(self, capacity):
		super(LastUpdatedOrdereDict, self).__init__()
		self._capacity = capacity
		
	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			print('remove:', last)
		if containsKey:
			del self[key]
			print('set:', (key, value))
		else:
			print('add:', (key, value))
		OrderedDict.__setitem__(self, key, value)

print('\n')

# Counter Counter是一个简单的计数器，例如统计字符出现的个数
# Counter实际上也是dict的一个子类
from collections import Counter
c = Counter()
for ch in 'programing':
	c[ch] = c[ch] + 1
print(c)