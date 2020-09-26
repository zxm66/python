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
# 这个备注是有问题的，任何类型的langrage都必须关系数据类型
var1 = (1,"hello world")

var2 = [1,"hello world"]

var3 = {1,"hello world"}


if var1[0] == var2[0]:
    pass
else:
    pass
for item in var2:
    pass
number = 0
while number < 9 :
    number = number + 1
