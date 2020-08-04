#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys 
 
reload(sys)
sys.setdefaultencoding('utf-8')
 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list1 = list(str(x))
        list2 = list(str(x))
        list2.reverse()
        result = True
        for index in range(len(list1)):
            if list1[index] != list2[index]:
                result = False
        return result


if __name__ == "__main__":
    print Solution().isPalindrome(1212)
    
