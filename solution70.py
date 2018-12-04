# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 12/4/18
-------------------------------------------------
   File Name：     solution70
   Description :
   Author :       zhaobx
   date：          12/4/18
-------------------------------------------------
   Change Activity:
                   12/4/18:
-------------------------------------------------
"""
import time
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        pre = 1
        now = 2
        cur = 0
        for i in range(3,n+1):
            cur = pre + now
            pre = now
            now = cur
        return cur
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

s = Solution()
print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))

print(s.climbStairs(4))
start = time.time()
print(s.climbStairs(35))
print(time.time() - start)