#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    通过用户名和密码上传下载文件到远程服务器
"""
import os, sys
import paramiko


t = paramiko.Transport(('192.168.15.15', 22))
t.connect(username='root', password='123456')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('log.txt', '/opt/log.txt')
t.close()
print '上传成功'
