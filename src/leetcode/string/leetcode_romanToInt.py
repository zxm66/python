#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        list1 = list(s)
        length = len(list1)
        if length == 1:
            return hashmap.get(list1[0])
        i = 0
        result = 0 
        while i < length - 1:
            key = list1[i] + list1[i+1]
            if hashmap.get(key) != None:
                result += hashmap.get(key)
                i += 2
            else:
                result += hashmap.get(list1[i])
                i += 1
            pass
        if length > 1 and hashmap.get(list1[length - 2] + list1[length - 1]) == None:
            result += hashmap.get(list1[length - 1])

        return result


if __name__ == "__main__":
    print Solution().romanToInt("VV")

