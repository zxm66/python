#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
 
######################################################################
# 
# Copyright (c) 2017 kinva.cc, Inc. All Rights Reserved
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
 
 
__import__('pprint').pprint("this is hello world")
# 不写mian和写上main方法的区别在于其他模块倒入程序的时候，要执行这段代码
if __name__ == '__main__':
    
    str1 = 'hello world'
    ch1 = 'c'
    number1 = 1
    number2 = 5555555
    number3 = 3.2
    number4 = 3.408000
    print ("hello world")
    print(id(str1))
    print(hex(id(str1)))

    pass
