#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入MySQL驱动
import mysql.connector

conn = mysql.connector.connect(user='root', password='password', database='test')
cursor = conn.cursor()

# 创建user表
cursor.execute(r"create table user (id varchar(20) primary key, name varchar(20))")

# 插入一行记录，注意MySQL的占位符是%s
cursor.execute(r"insert into user (id, name) values (%s, %s)", ['1', 'Michael'])
cursor.rowcount

# 提交事务
conn.commit()
cursor.close()

# 运行查询
cursor = conn.cursor()
cursor.execute(r"select * from user where id = %s", ('1',))
values = cursor.fetchall()
print(values)

# 关闭cursor connection
cursor.close()
conn.close()