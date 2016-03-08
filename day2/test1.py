#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    1 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
    2 即： {'k1': 大于66 , 'k2': 小于66}
"""
a = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# dict1 = {'k1': [], 'k2': []}
# for i in a:
#     if i > 66:
#         dict1['k1'].append(i)
#     else:
#         dict1['k2'].append(i)
#
# print dict1

# 动态扩展字典 更高效
dict1 = {}
for i in a:
    if i > 66:
        if 'k1' in dict1:
            dict1['k1'].append(i)
        else:
            dict1['k1'] = [i, ]
    else:
        if 'k2' in dict1:
            dict1['k2'].append(i)
        else:
            dict1['k2'] = [i, ]

print dict1
