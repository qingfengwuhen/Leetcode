# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 12/3/18
-------------------------------------------------
   File Name：     solution53
   Description :
   Author :       zhaobx
   date：          12/3/18
-------------------------------------------------
   Change Activity:
                   12/3/18:
-------------------------------------------------
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]

        tempSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            tempSum = max(nums[i], nums[i] + tempSum)
            maxSum = max(tempSum, maxSum)
        return maxSum

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        # if len(nums) == 1:
        #     return nums[0]

        tempSum = nums[0]
        maxSum = nums[0]
        for value in nums[1:]:
            tempSum = max(value, value + tempSum)
            maxSum = max(tempSum, maxSum)
        return maxSum

s = Solution()
print(s.maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))