# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 12/3/18
-------------------------------------------------
   File Name：     solution38
   Description :
   Author :       zhaobx
   date：          12/3/18
-------------------------------------------------
   Change Activity:
                   12/3/18:
-------------------------------------------------
"""
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        if n == 1:
            return s
        for i in range(1, n):
            symbol = ''
            count = 1
            tempString = []
            for j in range(1, len(s)):
                if s[j] == s[j-1]:
                    count+=1
                else:
                    symbol = s[j-1]
                    tempString.append(str(count)+symbol)
                    count = 1
            tempString.append(str(count) + s[-1])
            s = ''.join(tempString)

        return s
s = Solution()
print(s.countAndSay(1))
print(s.countAndSay(2))
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(5))
print(s.countAndSay(6))

