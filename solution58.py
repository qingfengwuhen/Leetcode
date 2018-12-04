# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 12/3/18
-------------------------------------------------
   File Name：     solution58
   Description :
   Author :       zhaobx
   date：          12/3/18
-------------------------------------------------
   Change Activity:
                   12/3/18:
-------------------------------------------------
"""
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastWordLength = 0
        start = 0
        for i in range(len(s)-1, -1, -1):

            if s[i] == ' ':
                if start:
                    return lastWordLength
            else:
                start = 1
                lastWordLength += 1
        return lastWordLength

s = Solution()
print(s.lengthOfLastWord("Hello world! "))