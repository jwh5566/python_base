#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
rand_num = random.randrange(10)

for i in range(3):
    guess_num = int(raw_input('请猜猜数字: '))
    if guess_num == rand_num:
        print '太棒了，猜对了'
        break
    elif guess_num > rand_num:
        print '你猜测的数字有对大了，请尝试小点的数字'
    else:
        print '你猜测的数字有对小了，请尝试大点的数字'
else:
    print '不要灰心，下次尝试'
print '真正的数字是:%d' % rand_num