#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        index = 0
        for item in strs:
            result += item[index]



        return result

if __name__ == "__main__":
    print Solution().longestCommonPrefix(["hello","hi"])
    
