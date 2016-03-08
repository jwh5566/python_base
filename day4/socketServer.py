#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket


sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(('127.0.0.1', 6666))
sk.listen(5)

while True:
    print '等待客户端连接...........'
    connection, address = sk.accept()
    client_message = connection.recv(1024)
    print '客户端发送信息', client_message
    connection.sendall('hello connect this server')
    connection.close()
