# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 12/3/18
-------------------------------------------------
   File Name：     solution28
   Description :
   Author :       zhaobx
   date：          12/3/18
-------------------------------------------------
   Change Activity:
                   12/3/18:
-------------------------------------------------
"""
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1 = len(haystack)
        l2 = len(needle)
        if l1 == 0 :
            if l2>0:
                return -1
            else:
                return 0

        if l2 == 0:
            return 0
        if l1 < l2:
            return -1
        i = 0
        while i < l1 - l2+1:
            commonFlag = 1
            for j in range(l2):
                if haystack[i+j] != needle[j]:
                    commonFlag = 0
                    break
            if commonFlag:
                return i
            else:
                i += 1
        return -1

s = Solution()
print(s.strStr("a", "a"))