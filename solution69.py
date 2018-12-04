# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 12/4/18
-------------------------------------------------
   File Name：     solution69
   Description :
   Author :       zhaobx
   date：          12/4/18
-------------------------------------------------
   Change Activity:
                   12/4/18:
-------------------------------------------------
"""
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        rootUnderHundred = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        firstDigit = 0
        if x == 0:
            return 0
        if x == 1:
            return 1
        digitsLenght = -1
        temp = x
        l = []
        while temp > 0:
            l.insert(0, temp % 100)
            temp = temp // 100
            digitsLenght += 1
        print(l, digitsLenght)
        if l[0] >= 81:
            firstDigit = 9
        elif l[0] >= 64:
            firstDigit = 8
        elif l[0] >= 49:
            firstDigit = 7
        elif l[0] >= 36:
            firstDigit = 6
        elif l[0] >= 25:
            firstDigit = 5
        elif l[0] >= 16:
            firstDigit = 4
        elif l[0] >= 9:
            firstDigit = 3
        elif l[0] >= 4:
            firstDigit = 2
        else:
            firstDigit = 1
        upperBound = firstDigit * 10 ** digitsLenght + 10 ** digitsLenght - 1
        lowerBound = firstDigit * 10 ** digitsLenght
        print(lowerBound, upperBound)
        count = 0
        while lowerBound < upperBound:
            count += 1
            print(count)
            mid = (upperBound + lowerBound) // 2
            a = mid * mid -x
            b = (mid + 1) * (mid + 1) - x
            if a * b <= 0:
                break
            if a > 0:
                upperBound = mid -1
            else:
                lowerBound = mid + 1
        else:
            return lowerBound

        if b == 0:
            return mid + 1
        else:
            return mid

s = Solution()
print(s.mySqrt(99991111111))
