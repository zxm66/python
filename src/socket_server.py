#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

s = socket.socket()
hostname = socket.gethostname()
port = 1234
s.bind((hostname,port))
s.listen(5)
while True:
    c,addr = s.accept()
    print addr
    c.send("hello world")
    c.close()
