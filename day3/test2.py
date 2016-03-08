#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.15.15', 22, 'root', '123456')
stdin, stdout, stderr = ssh.exec_command('df -h')
print stdout.read()
ssh.close()


