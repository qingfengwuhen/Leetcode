# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 12/3/18
-------------------------------------------------
   File Name：     solution35
   Description :
   Author :       zhaobx
   date：          12/3/18
-------------------------------------------------
   Change Activity:
                   12/3/18:
-------------------------------------------------
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l1 = len(nums)
        if l1  == 0:
            return 0
        if target <= nums[0]:
            return 0

        for i in range(l1):
            if target <= nums[i]:
                return i
        return l1

s = Solution()
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))
print(s.searchInsert([1,3,5,6], 0))
