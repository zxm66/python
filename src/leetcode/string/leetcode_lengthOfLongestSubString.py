#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 1
        list1 = list(s)
        for i in range(len(s)):
            for j in range(i + 1 ,len(s)):
                if list1[i] != list1[j]:
                    length += 1
                pass
            pass
        return length
if __name__ == "__main__":
    print len("hello world")
    print list("hello world")
    pass
