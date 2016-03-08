#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    文本块生成器
"""


# 生成器返回一行+\n
def lines(file):
    for line in file: yield line
    yield '\n'


# 返回块
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:  # 遇到空行
            yield ''.join(block).strip()  # 将元素拼接 返回块
            block = []

# f = open(r'C:\test\test_input.txt')
# result = blocks(f)
# print result.next()
# print result.next()
# print result.next()
# print result.next()


