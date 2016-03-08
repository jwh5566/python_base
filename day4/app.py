#!/usr/bin/env python
# -*- coding: utf-8 -*-

str = 'AHWHbiyun'

print "*"*15+"业主端"+"*"*15
s1 = 'comyucitestzhsqstoreconsumer1'
print s1.replace('yucitest', str)

s2 = 'com.yucitest.zhsq.store.consumer1'
print s2.replace('yucitest', str)
print
print "*"*15+"物业端"+"*"*15
s5 ='comhousemanageYUCITEST'
print s5.replace('YUCITEST', str)

s6 ='com.housemanage.YUCITEST'
print s6.replace('YUCITEST', str)

print
print "*"*15+"商家端"+"*"*15
s3 ='comhousemanageebusinessYUCITEST'
print s3.replace('YUCITEST', str)

s4 ='com.housemanage.ebusiness.YUCITEST'
print s4.replace('YUCITEST', str)