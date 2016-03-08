#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    简单身份认证
"""
user_info = {
    "zhangsan": "123456",
    "lisi": "123456",
    "wangwu": "123456"
}


def login_auth():
    user_input = raw_input("\033[32;1m请输入您的用户名 :\033[0m")
    pass_input = raw_input("\033[32;1m请输入您的密码 :\033[0m")

    if user_info.get(user_input):
        if pass_input == user_info[user_input]:
            print "\033[32;1m登录成功\033[0m"
        else:
            print "\033[31;1m密码错误\033[0m"
    else:
        print "\033[31;1m您输入的用户名不存在\033[0m"

login_auth()
