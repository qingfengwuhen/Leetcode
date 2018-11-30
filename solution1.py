# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 6/20/18
-------------------------------------------------
   File Name：     solution1
   Description :
   Author :       zhaobx
   date：          6/20/18
-------------------------------------------------
   Change Activity:
                   6/20/18:
-------------------------------------------------
"""
import numpy as np
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                x=nums[i]
                y=nums[j]
                if x+y==target:
                    return [i,j]

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapDic={}
        i=0
        for num in nums:
            complement=target-num
            if complement in mapDic:
                return([i, mapDic.get(complement)])
            mapDic[num] = i
            i+=1
            # print(mapDic)

# public int[] twoSum(int[] nums, int target) {
#     Map<Integer, Integer> map = new HashMap<>();
#     for (int i = 0; i < nums.length; i++) {
#         map.put(nums[i], i);
#     }
#     for (int i = 0; i < nums.length; i++) {
#         int complement = target - nums[i];
#         if (map.containsKey(complement) && map.get(complement) != i) {
#             return new int[] { i, map.get(complement) };
#         }
#     }
#     throw new IllegalArgumentException("No two sum solution");
# }
# public int[] twoSum(int[] nums, int target) {
#     Map<Integer, Integer> map = new HashMap<>();
#     for (int i = 0; i < nums.length; i++) {
#         int complement = target - nums[i];
#         if (map.containsKey(complement)) {
#             return new int[] { map.get(complement), i };
#         }
#         map.put(nums[i], i);
#     }
#     throw new IllegalArgumentException("No two sum solution");
# }

nums = [2, 4, 11, 15, 6]
target=8
p = Solution()
print(p.twoSum2(nums,target))