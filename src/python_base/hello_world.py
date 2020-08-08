#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
######################################################################
# 
# Copyright (c) 2017 kinva.cc, Inc. All Rights Reserved
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
# import
import sys 
 
# 
reload(sys)

# set default encoding 
sys.setdefaultencoding('utf-8')
 
if __name__ == '__main__':
    obj = __import__('pprint')
    __import__('pprint').pprint('hello world')
    list = [1,2]
    __import__('pprint').pprint(list[0])
    if True:
        __import__('pprint').pprint('this is true')
    else:
        __import__('pprint').pprint('this is flase')
    obj.pprint('this is obj')
    number = 1
    number1 = 2
    obj.pprint(number+number1)
    print 'hello world'
    print 'hello world'
    list1 = [1,2,3,4,4]
    for item in list1:
        print item

