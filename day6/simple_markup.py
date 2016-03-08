#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re
from utils import *


f = open(r'C:\test\test_input.txt')
print '<html><head><title>...</title><body>'

title = True
for block in blocks(f):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)   # 过滤被*包含的文本
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'
print '</body></html>'
f.close()

