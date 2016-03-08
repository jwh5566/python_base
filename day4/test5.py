#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root123',db='douban', charset='utf8')
cur = conn.cursor()

sql = 'select * from book_list'
reCount = cur.execute(sql)
print 'there has %s rows record' % reCount

# result = cur.fetchone()
# print result
# print 'name: %s' % result
results = cur.fetchall()
for r in results:
    print r[0]


