#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
"""
    数据库相关
"""

connection = MySQLdb.connect(host="localhost", user="root", passwd="root123", db="douban", port=3306, charset="utf8")
cursor = connection.cursor()
for i in range(20):
    value = i
    sql_res = cursor.execute('insert into book_list VALUES(%s)', value)
connection.commit()
cursor.close()
connection.close()



