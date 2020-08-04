#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
s = socket.socket()

hostname = socket.gethostname()
port = 1234

s.connect((hostname,port))

print s.recv(1024)
s.close()
