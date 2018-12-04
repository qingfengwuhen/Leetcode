# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 12/4/18
-------------------------------------------------
   File Name：     solution67
   Description :
   Author :       zhaobx
   date：          12/4/18
-------------------------------------------------
   Change Activity:
                   12/4/18:
-------------------------------------------------
"""
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        # """
        # def add(a, b, c=0):
        #     sum = a + b + c
        #     return sum//2, sum%2
        l1 = len(a)
        l2 = len(b)
        if l1 < l2:
            a, b = b, a
            l1, l2 = l2, l1
        l = ''
        dic = {'00':('0', '0'), '01':('0','1'), '10':('0', '1'), '11':('1', '0')}
        c = '0'
        j = l2-1
        for i in reversed(range(0, l1)):
            if j >= 0:
                c1, v = dic[c+a[i]]
                c2, v = dic[b[j] + v]
                v2, c = dic[c1 + c2]
            else:
                c, v = dic[c + a[i]]
            j -= 1
            l = v + l
        if c == '1':
            l = c + l
        # print(l)
        return l


        # return a + b



s = Solution()
print(s.addBinary('111', '111'))
print(s.addBinary('1010', '1011'))
