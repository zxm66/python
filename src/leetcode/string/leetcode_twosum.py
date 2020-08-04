#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list1 = []
        for index1 in range(len(nums)):
            for index2 in range(index1+1,len(nums)):
                if (nums[index1]+nums[index2]) == target:
                    list1.append(index1)
                    list1.append(index2)
                pass
            pass
        return list1


if __name__ == "__main__":
    nums = [1,2,3]
    target = 3
    print Solution().twoSum(nums,target)
    pass
