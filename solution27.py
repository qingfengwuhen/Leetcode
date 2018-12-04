# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 12/3/18
-------------------------------------------------
   File Name：     solution27
   Description :
   Author :       zhaobx
   date：          12/3/18
-------------------------------------------------
   Change Activity:
                   12/3/18:
-------------------------------------------------
"""
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        j = 0
        for i in range(l):
            if nums[i-j] == val:
                nums.pop(i-j)
                j += 1
        # print(nums)
        return j
    def popInfluence(self, nums):
        print(len(nums))
        for i in range(len(nums)):
            print(nums)
            if i % 2 == 1:
                nums.pop()
        print(nums)

s = Solution()
# s.popInfluence([0,0,1,1,1,2,2,3,3,4])
print(s.removeElement([0,0,1,1,1,2,2,3,3,4], 1))