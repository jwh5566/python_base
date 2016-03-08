#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket


ck = socket.socket()
ck.connect(('127.0.0.1', 6666))
ck.sendall('hello server, this is client')
server_answer = ck.recv(1024)
print server_answer
ck.close()
