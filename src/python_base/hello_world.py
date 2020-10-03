#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
 
######################################################################
# 
# Copyright (c) 2017 kinva.cc, Inc. All Rights Reserved
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
 
 
"""
    hello zhangxiaomin
    python基础学习，已经学习完成了。现在我的总结一下了。

"""

__import__('pprint').pprint("this is hello world")
# 不写mian和写上main方法的区别在于其他模块倒入程序的时候，要执行这段代码
if __name__ == '__main__':
    """
    hello world
    """

    str1 = 'hello world'
    print(type(str1))
    ch1 = 'c'
    print(type(ch1))
    number1 = 1
    print(type(number1))
    number2 = 5555555
    print(type(number2))
    number3 = 3.2
    print(type(number3))
    number4 = 3.408000
    print(type(number4))
    print ("hello world")
    print(id(str1))
    print(hex(id(str1)))
    print(type.__class__)

    pass
