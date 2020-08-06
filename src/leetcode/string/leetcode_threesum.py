#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        print nums
        length = len(nums)
        for i in range(length):
            for j in range(i+1,length):
                for k in range(j+1,length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        item = [nums[i],nums[j],nums[k]]
                        item.sort()
                        if item not in result:
                            result.append(item)
        return result
if __name__ == "__main__":
    list1 = [1,2,3]
    print Solution().threeSum(list1)
    pass
