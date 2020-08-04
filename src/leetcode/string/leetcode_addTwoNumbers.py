#!/usr/bin/env python
# -*- coding:utf-8 -*-



class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
    def __toString__(self):
        print self.val
        tmpNext = self.next
        while(tmpNext != None):
            print tmpNext.val
            tmpNext = tmpNext.next
        pass
class Solution(object):
    def addTwoNumbers(self, l1,l2):
        """TODO: Docstring for addTwoNumbers.
        :function: ListNode
        :returns: ListNode
        """
        value1 = 0
        value2 = 0
        ln = ln1 = ListNode(0)
        while(l1 != None):
            value = l1.val + l2.val + value2
            value1 = value % 10
            value2 = value / 10
            ln.val = value1
            l1 = l1.next
            l2 = l2.next
            if l1 != None:
                ln.next = ListNode(0)
                ln = ln.next
        return ln1
if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)
    Solution().addTwoNumbers(l1,l2).__toString__()
        
