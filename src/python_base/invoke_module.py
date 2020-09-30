#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
######################################################################
# 
# Copyright (c) 2017 kinva.cc, Inc. All Rights Reserved
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
 

import support_module
#from support_module import *

# __name__ 当直接运行py文件的时候这个值等于__main__ 当导入py文件的时候这个值等于文件名
if __name__ == "__main__":
    support_module.support_print("hello world")
    print(support_module.hello)
    print(support_module.world)   
    pass
