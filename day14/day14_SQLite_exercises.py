#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3, os

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
	os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute(r"select name, score from user where score between ? and ? order by score", (low, high))
	result = cursor.fetchall()
	cursor.close()
	conn.close()
	print(result)
	print([x[0] for x in result])
get_score_in(0, 100)