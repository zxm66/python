#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
######################################################################
# 
# Copyright (c) 2017 kinva.cc, Inc. All Rights Reserved
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
 

# python langrage don't care the type of data

var1 = (1,"hello world")
print var1

var2 = [1,"hello world"]
print var2

var3 = {1,"hello world"}
print var3

print var1[0]+var2[0]+list(var3)[0]

if var1[0] == var2[0]:
    print "var1[0] is equals var2[0]"
else:
    print "var1[0] is not equals var2[0]"

for item in var2:
    print item

number = 0
while number < 9 :
    print number
    number = number + 1
