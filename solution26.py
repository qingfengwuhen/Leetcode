# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 12/3/18
-------------------------------------------------
   File Name：     solution26
   Description :
   Author :       zhaobx
   date：          12/3/18
-------------------------------------------------
   Change Activity:
                   12/3/18:
-------------------------------------------------
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return []
        pre = nums[0] - 1
        i = 0
        l = len(nums)
        j = 0
        while i < l:
            if i + j >= l:
                break
            if pre == nums[i]:
                nums.pop(i)
                j += 1
                # i += 1
                continue
            i += 1
            pre = nums[i-1]
        return nums
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return []
        pre = nums[0]
        j = 1
        for data in nums:
            if data != pre:
                nums[j] = data
                pre = nums[j]
                j += 1
        return j, nums
    def removeDuplicates3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        pre = nums[0]
        j = 1
        notchange = 0
        for data in nums:
            if data != pre:
                if notchange:
                    nums[j] = data
                pre = data
                j += 1

            else:
                notchange = 1
        return j, nums
s = Solution()
print(s.removeDuplicates([1,1,2]))
print(s.removeDuplicates2([0,0,1,1,1,2,2,3,3,4]))
print(s.removeDuplicates3([0,0,1,1,1,2,2,3,3,4]))
