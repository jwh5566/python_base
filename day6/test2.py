#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import MySQLdb as mysql


db = mysql.connect(user='root', passwd='root123', db='douban', host='127.0.0.1')
db.autocommit(True)
cur = db.cursor()


def getMem():
    with open('/proc/meminfo') as f:
        total = int(f.readline().split()[1])
        free = int(f.readline().split()[1])
        buffers = int(f.readline().split()[1])
        cache = int(f.readline().split()[1])
    mem_use = total-free-buffers-cache
    # print mem_use/1024
    t = int(time.time())
    sql = 'insert into memory VALUES (%s,%s)' %(mem_use/1024, t)
    cur.execute(sql)
    print mem_use/1024
while True:
    time.sleep(1)
    getMem()
