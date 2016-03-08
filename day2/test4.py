#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    装饰器演示
"""


def w1(func):
    def inner(*args, **kwargs):
        print '函数执行前1'
        func(*args, **kwargs)
        print '函数执行后2'
    return inner


def w2(func):
    def inner(*args, **kwargs):
        print '函数执行前3'
        func(*args, **kwargs)
        print '函数执行后4'
    return inner


@w1
@w2
def f1(arg1, arg2, arg3):
    print arg1, arg2, arg3

f1('nihao', 'jwh5566', 'shuaige')
