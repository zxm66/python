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
 
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
    def __toString__(self):
        ln = self
        while ln != None:
            print ln.val
            ln = ln.next
class Solution(object):
    def addTwoNumbers(self,l1,l2):
        value1 = 0
        value2 = 0
        ln1 = ln = ListNode(0)
        while l1 != None and l2 != None:
            value = l1.val + l2.val + value2
            value1 = value % 10
            value2 = value / 10
            ln.val = value1
            l1 = l1.next
            l2 = l2.next
            if l1 != None and l2 != None:
                ln.next = ListNode(0)
                ln = ln.next
            pass
        while l1 != None:
            value = l1.val + value2
            value1 = value % 10
            value2 = value / 10
            ln.next = ListNode(value1)
            ln = ln.next
            l1 = l1.next
            pass
        while l2 != None:
            value = l2.val + value2
            value1 = value % 10
            value2 = value / 10
            ln.next = ListNode(value1)
            ln = ln.next
            l2 = l2.next
            pass
        if value2 != 0:
            ln.next = ListNode(value2)
            ln = ln.next
        return ln1
        
if __name__ == '__main__':
    ln1 = ListNode(1)
    ln1.next = ListNode(2)


    ln2 = ListNode(9)
    ln2.next = ListNode(7)
    ln2.next.next = ListNode(2)
    
    ln3 = ListNode(5)
    ln4 = ListNode(5)
    Solution().addTwoNumbers(ln1,ln2).__toString__()
    pass 


