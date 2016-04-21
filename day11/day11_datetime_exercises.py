#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# str to timestamp

from datetime import datetime, timezone, timedelta
import re

def to_timestamp(dt_str, tz_str):
	re_tz = re.match(r'^[UTC]{3}([+-]\d{1,2})\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', tz_str)
	tz_utc = timezone(timedelta(hours=int(re_tz.group(1)), minutes=int(re_tz.group(2))))
	dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
	result_dt = dt.replace(tzinfo=tz_utc).astimezone(timezone(timedelta(hours=0)))
	return result_dt.timestamp()
	
	
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print(t1, '\n', t2)
