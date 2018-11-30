# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 6/20/18
-------------------------------------------------
   File Name：     solution3
   Description :
   Author :       zhaobx
   date：          6/20/18
-------------------------------------------------
   Change Activity:
                   6/20/18:
-------------------------------------------------
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # print(s)
        lens=len(s)
        # print(lens)
        longestStr=[]

        length=0
        for i in range(lens):
            index=i
            char = s[i]
            temp = []
            while char not in temp:
                temp.append(char)
                index+=1
                if index>=lens:
                    break
                char = s[index]
            if len(temp)>length:
                longestStr=temp
                length=len(temp)
        return len(longestStr)
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # print(s)
        lens=len(s)
        longestStr=[]
        temp = []
        length=0
        for i in range(lens):
            char = s[i]
            if char not in temp:
                temp.append(char)
            else:
                index=temp.index(char)
                temp=temp[index+1:]
                temp.append(char)
            if len(temp)>length:
                longestStr=temp
                length=len(temp)
        return len(longestStr)




p = Solution()
s='abcabcbb'
print(p.lengthOfLongestSubstring(s))
s='bbbbb'
print(p.lengthOfLongestSubstring(s))
s='pwwkew'
print(p.lengthOfLongestSubstring(s))
