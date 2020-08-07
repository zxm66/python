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
 
class Solution(object):
    def reverseString(self,s):
        i ,j = 0 ,len(s) - 1
        while(i < j):
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        print s
if __name__ == '__main__':
    Solution().reverseString(["hello", "world"])


