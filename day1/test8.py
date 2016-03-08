#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 标志位 可以返回上层循环
import time
count = 0
while True:
    print '我是第一层'
    time.sleep(2)
    jump_1_flag = False
    while True:
        print '我是第二层'
        time.sleep(2)
        jump_2_flag = False
        while True:
            count += 1
            print '我是第三层'
            time.sleep(2)
            if count > 3:
                jump_2_flag = True
                break
        if jump_2_flag:
            print '我从第三层跳到这里来了，我也要跳到第一层'
            time.sleep(2)
            jump_1_flag = True
            break
    if jump_1_flag:
        print '我从第二层跳过来的'
        time.sleep(2)
        break
