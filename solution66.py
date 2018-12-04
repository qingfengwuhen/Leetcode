# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 12/4/18
-------------------------------------------------
   File Name：     solution66
   Description :
   Author :       zhaobx
   date：          12/4/18
-------------------------------------------------
   Change Activity:
                   12/4/18:
-------------------------------------------------
"""
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        l=[]
        j = 0
        for data in reversed(digits):
            if j == 0:
                sum_now = data + 1 + carry
            else:
                sum_now = data + carry
            j += 1
            carry = sum_now // 10

            l.insert(0, sum_now%10)
        if sum_now == 10:
            l.insert(0, 1)
        return l

s = Solution()
print(s.plusOne([4,3,2,1]))
print(s.plusOne([4,3,9,9]))
print(s.plusOne([4,9,9,9]))
print(s.plusOne([9,9,9,9]))