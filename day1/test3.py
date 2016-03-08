#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    获取豆瓣书籍的名称
"""
import urllib
import MySQLdb
from bs4 import BeautifulSoup


res = urllib.urlopen("http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book")
soup = BeautifulSoup(res)
book_div = soup.find(attrs={"id": "book"})
book_a = book_div.findAll(attrs={"class": "title"})
for book in book_a:
    print book.string


