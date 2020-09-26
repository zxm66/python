#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
######################################################################
# 
# Copyright (c) 2017 kinva.cc, Inc. All Rights Reserved
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
 
 
 
from pprint import pprint


if __name__ == '__main__':
    try:
        file = open('1.txt','w')
        file.write("hello world")

        file = open('1.txt','r')
        current = file.readline();
        pprint("this current is {}".format(current))
    except Exception as e:
        raise e

