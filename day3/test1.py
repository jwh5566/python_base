#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    便捷日志记录模块
"""
import logging


def log_models(logname, infos):
    logger = logging.getLogger(logname)  # 定义用户名
    logger.setLevel(logging.DEBUG)  # 定义全局日志级别

    ch = logging.StreamHandler()  # 定义屏幕日志
    ch.setLevel(logging.DEBUG)  # 屏幕日志级别

    fh = logging.FileHandler('log.txt')  # 日志保存文件
    fh.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)  # 屏幕输出日志格式
    fh.setFormatter(formatter)  # 文件输出日志格式

    logger.addHandler(ch)  # 屏幕输出日志交给logger接口执行
    logger.addHandler(fh)
    logger.debug(infos)


log_models('jwh5566', 'the server is down')
