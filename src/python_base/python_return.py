#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
######################################################################
# 
# Copyright (c) 2017 kinva.cc, Inc. All Rights Reserved
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
 
import sys 
 
reload(sys)
sys.setdefaultencoding('utf-8')
 
def test_return():
    return 1,"hello world"
if __name__ == '__main__':
    number,string = test_return()
    print number,string


