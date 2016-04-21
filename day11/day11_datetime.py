#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# datetime
from datetime import datetime


# 获取当前日期和时间
now = datetime.now()
print(now)
print(type(now), '\n')


# 获取指定日期和时间
dt = datetime(2015, 4, 19, 20, 8)
print(dt, '\n')

# datetime 转换为 timestamp
print(dt.timestamp(), '\n')

# timestamp转换为datetime
t = 12352435243.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t), '\n')

# str 转换 datetime
cday = datetime.strptime('2016-4-22 10:21', '%Y-%m-%d %H:%M')
print(cday, '\n')

# datetime 转换为 str
nowtime = datetime.now()
print(now.strftime('%a, %y %b, %Y %m %d %H:%M:%S'), '\n')

# datetime加减
from datetime import timedelta
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=0.5))
print(now - timedelta(days=2, hours=8))
print('\n')

# 本地时间转换为UTC时间

from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))# 创建时区UTC+8:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt, '\n')

# 时区转换
# 我们可以通过utcnow()拿到当前的UTC时间,再转换为任意时区的时间
# 拿到UTC时间，并强制设置时区为UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

print(datetime.utcnow())
# astimezone()将时区转换为北京时间 
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)




