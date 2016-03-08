#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.15.15', port=22, username='root', password='123456')
stdin, stdout, stderror = ssh.exec_command('ifconfig')

print stdout.read()
ssh.close()
