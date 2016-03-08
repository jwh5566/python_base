#!/usr/bin/env python
# -*- coding:utf-8 -*-

user_info = {
            "zhangsan":"mima1",
            "lisi":"mima2",
            "wangwu":"mima3",
}


def login_auth(): #定义一个函数
    user_input = raw_input("\033[32;1m请输入您的用户名：\033[0m") #获取用户的用户名
    pass_input = raw_input("\033[32;1m请输入您的密码：\033[0m")#获取用户输入的密码

    if user_info.get(user_input):     #判断用户名是否存在，如果存在判断密码是否正确！
        if pass_input == user_info[user_input]: #判断用户输入的密码和存储的用户密码是否匹配
            return True
        else:
            return False
    else:
        return False


def wrapper(func):
    def inner():
        if login_auth(): #如果登录成功回返回True然后执行func函数（func=被装饰的函数）
            func()
        else:
            return "\033[32;1m登录失败\033[0m"
    return inner


@wrapper
def func1():
    print "hello This is Func1"


@wrapper
def func2():
    print "hello This is Func2"


@wrapper
def func3():
    print "hello This is Func3"


@wrapper
def func4():
    print "hello This is Func4"

func1()
func2()
func3()
func4()
