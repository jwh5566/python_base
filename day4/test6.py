#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root123',db='douban', charset='utf8')
cur = conn.cursor()


cur.execute("insert into book_list values('姜')")
conn.commit()
cur.close()
conn.close()
