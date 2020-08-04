#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str1 = str(x)
        list1 = list(str1)
        maxIndex = len(list1) - 1
        result = ""
        if list1[0] == "-":
            result = "-"
        while(maxIndex > 0):
            result += list1[maxIndex]
            maxIndex -= 1
            pass
        if list1[0] != "-":
            result += list1[0]
        print result
        y = int(result)
        if y > -2**31 and y < 2**31 -1:
            return y
        else:
            return 0
if __name__ == "__main__":
    s = Solution()
    print s.reverse(1534236469)
    pass
