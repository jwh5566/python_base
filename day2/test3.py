#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    1 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
    2 即： {'k1': 大于66 , 'k2': 小于66}
"""
from collections import OrderedDict, defaultdict, Counter

# c = Counter('abcdeabcab')
# print c

# defaultdict （ 默认给字典的值设置了一个类型）
values = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
my_dict = defaultdict(list)

for value in values:
    if value > 66:
        my_dict['k1'].append(value)
    else:
        my_dict['k2'].append(value)

print my_dict
