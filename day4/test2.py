#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Shuaigeerror(Exception):
    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        if self.msg:
            return self.msg
        else:
            return 'something error'

try:
    raise Shuaigeerror('shuaige is handsome')
except Exception, e:
    print e