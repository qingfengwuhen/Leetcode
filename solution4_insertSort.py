# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 11/30/18
-------------------------------------------------
   File Name：     solution4_insertSort
   Description :
   Author :       zhaobx
   date：          11/30/18
-------------------------------------------------
   Change Activity:
                   11/30/18:
-------------------------------------------------
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        m = len(nums1)
        n = len(nums2)
        l = m + n
        if l % 2 == 1:
            maxNum = nums1.pop() if nums1[-1] > nums2[-1] else nums2.pop()
            midk = (l-1) // 2
        else:
            midK = l // 2 - 1





    def findMedianSortedArrays2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        m = len(nums1)
        n = len(nums2)
        l = m + n
        for i in range(l):
            if len(nums1) == 0:
                nums.append(nums2)
                break
            if len(nums2) == 0:
                nums.append(nums1)
                break
            if nums1[0] <= nums2[0]:
                nums.append(nums1.pop(0))
            else:
                nums.append(nums2.pop(0))

        if (l) % 2 == 1:
            return nums[(l - 1) // 2]
        else:
            return (nums[l // 2] + nums[l // 2 - 1])/2

def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0


p = Solution()
nums1 = [1, 2, 4, 8, 9, 10, 15, 16]
nums2 = [3, 4, 5, 7, 8, 9, 10, 11, 12, 13]
# nums1 = [2,5]
# nums2 = [3,4]
print(nums1)
print(nums2)
mid=p.findMedianSortedArrays(nums1, nums2)
print(mid)

print(median(nums1, nums2))