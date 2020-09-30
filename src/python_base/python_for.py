#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
 
######################################################################
# 
# Copyright (c) 2017 kinva.cc, Inc. All Rights Reserved
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
 
 
if __name__ == '__main__':
    
    for letter in "python":
        __import__('pprint').pprint("this letter is {}".format(letter))
    var1 = {"name":"zhangxiaomin","age":18}

    for key in var1.keys():
        __import__('pprint').pprint("this key is {}".format(key))
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i!=j and j!=k and i!=k:
                    print i,j,k

    for item in [1,2,3]:
        pass
    step = 2
    for item in range(0,10,step):
        pass
