# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 6/21/18
-------------------------------------------------
   File Name：     solution4
   Description :
   Author :       zhaobx
   date：          6/21/18
-------------------------------------------------
   Change Activity:
                   6/21/18:
-------------------------------------------------
"""



class Solution(object):



    def findMedianSortedArrays_print(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=nums1+nums2
        print(nums)
        print(sorted(nums))
        sortedNums=sorted(nums)
        print(sortedNums)


        lenAll=len(nums)
        nums = [0] * lenAll
        print(lenAll)
        maxindex = lenAll
        minindex = 0

        midindex1 = findMedianSortedArrays3(nums1)
        print(midindex1)
        midindex2 = findMedianSortedArrays3(nums2)
        print(midindex2)
        i=0

        while len(nums1)>1 or len(nums2)>1:
            op = [[0] * 2 for row in range(2)]
            if midindex1[0]<midindex2[0]:
                nums[minindex:minindex+round(midindex1[2]+.1)] = nums1[0:round(midindex1[2]+.1)]
                nums1=nums1[round(midindex1[2]+.1):]
                minindex=minindex+round(midindex1[2]+.1)
                op[0][0]=1
            elif midindex1[0]>midindex2[0]:
                nums[minindex:minindex + round(midindex2[2] + .1)] = nums2[0:round(midindex2[2] + .1)]
                nums2 = nums2[round(midindex2[2] + .1):]
                minindex = minindex + round(midindex2[2] + .1)
                op[1][0]=1
            if midindex1[1]>midindex2[1]:
                nums[maxindex-round(midindex1[2]+.1):maxindex] = nums1[round(midindex1[2]+.51):]
                nums1=nums1[:round(midindex1[2]+.51)]
                maxindex=maxindex-round(midindex1[2]+.1)
                op[0][1]=1
            elif midindex1[1]< midindex2[1]:
                nums[maxindex - round(midindex2[2] + .1):maxindex] = nums2[round(midindex2[2] + .51):]
                nums2 = nums2[:round(midindex2[2] + .51)]
                maxindex=maxindex - round(midindex2[2] + .1)
                op[1][1]=1

            if midindex1[0] == midindex2[0] and midindex1[1] == midindex2[1]:
                return (midindex1[0]+midindex1[1])/2
            if midindex1[0] == midindex2[0]:
                if op[0][1]==1:
                    nums[minindex:minindex + round(midindex2[2] + .1)] = nums2[0:round(midindex2[2] + .1)]
                    nums2 = nums2[round(midindex2[2] + .1):]
                    minindex = minindex + round(midindex2[2] + .1)
                    op[1][0] = 1
                else:
                    nums[minindex:minindex + round(midindex1[2] + .1)] = nums1[0:round(midindex1[2] + .1)]
                    nums1 = nums1[round(midindex1[2] + .1):]
                    minindex = minindex + round(midindex1[2] + .1)
                    op[0][0] = 1
            if midindex1[1] == midindex2[1]:
                if op[0][0]==1:
                    nums[maxindex - round(midindex2[2] + .1):maxindex] = nums2[round(midindex2[2] + .51):]
                    nums2 = nums2[:round(midindex2[2] + .51)]
                    maxindex = maxindex - round(midindex2[2] + .1)
                    op[1][1] = 1
                else:
                    nums[maxindex - round(midindex1[2] + .1):maxindex] = nums1[round(midindex1[2] + .51):]
                    nums1 = nums1[:round(midindex1[2] + .51)]
                    maxindex = maxindex - round(midindex1[2] + .1)
                    op[0][1] = 1
            if sum(op[0][:]) == 2:
                print('finished')

            if sum(op[1][:]) == 2:
                print('finished')
            # if len(nums)==15:
            #     print('break')
            # i+=1
            # if i==3:
            #     print('break')
            # print(nums)
            midindex1 = findMedianSortedArrays3(nums1)
            print(midindex1)
            midindex2 = findMedianSortedArrays3(nums2)
            print(midindex2)
        print(nums, minindex, maxindex)
        nums[minindex]=min(nums1+nums2)
        nums[minindex+1] = max(nums1+nums2)
        print(nums)
        print(sortedNums)
        if lenAll%2==1:
            return nums[(lenAll + 1) / 2]
        else:
            return (nums[lenAll / 2] + nums[lenAll / 2 + 1]) / 2
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=nums1+nums2
        lenAll=len(nums)

        nums = [0] * lenAll
        print('nums is:', nums)
        maxindex = lenAll
        minindex = 0
        if len(nums1) == 0:
            return findMedianSortedArrays2(nums2)
        if len(nums2) == 0:
            return findMedianSortedArrays2(nums1)
        midindex1 = findMedianSortedArrays3(nums1)
        midindex2 = findMedianSortedArrays3(nums2)
        while len(nums1)>1 or len(nums2)>1:
            op = [[0] * 2 for row in range(2)]
            # if midindex1[0] + midindex1[1] == midindex2[0] + midindex2[1]:
            #     print('shortpath')
            #     return (midindex1[0] + midindex1[1]) / 2
            #     print('')

            if midindex1[0]<midindex2[0]:
                nums[minindex:minindex+round(midindex1[2]+.1)] = nums1[0:round(midindex1[2]+.1)]
                nums1=nums1[round(midindex1[2]+.1):]
                minindex=minindex+round(midindex1[2]+.1)
                op[0][0]=1
            elif midindex1[0]>midindex2[0]:
                nums[minindex:minindex + round(midindex2[2] + .1)] = nums2[0:round(midindex2[2] + .1)]
                nums2 = nums2[round(midindex2[2] + .1):]
                minindex = minindex + round(midindex2[2] + .1)
                op[1][0]=1
            if midindex1[1]>midindex2[1]:
                if op[0][0]==1:
                    nums[maxindex - round(midindex1[2] + .1):maxindex] = nums1[round(midindex1[2] + .51)-round(midindex1[2]+.1):]
                    nums1 = None
                    maxindex = maxindex - round(midindex1[2] + .1)
                else:
                    nums[maxindex-round(midindex1[2]+.1):maxindex] = nums1[round(midindex1[2]+.51):]
                    nums1=nums1[:round(midindex1[2]+.51)]
                    maxindex=maxindex-round(midindex1[2]+.1)
                op[0][1]=1
            elif midindex1[1]< midindex2[1]:


                if op[1][0] == 1:
                    nums[maxindex - round(midindex2[2] + .1):maxindex] = nums2[round(midindex2[2] + .51)-round(midindex2[2] + .1):]
                    nums2 = None
                    maxindex=maxindex - round(midindex2[2] + .1)
                else:
                    nums[maxindex - round(midindex2[2] + .1):maxindex] = nums2[round(midindex2[2] + .51):]
                    nums2 = nums2[:round(midindex2[2] + .51)]
                    maxindex = maxindex - round(midindex2[2] + .1)
                op[1][1]=1

            if midindex1[0] == midindex2[0] and midindex1[1] == midindex2[1]:
                return (midindex1[0]+midindex1[1])/2
            if midindex1[0] == midindex2[0]:
                if op[0][1]==1:
                    nums[minindex:minindex + round(midindex2[2] + .1)] = nums2[0:round(midindex2[2] + .1)]
                    nums2 = nums2[round(midindex2[2] + .1):]
                    minindex = minindex + round(midindex2[2] + .1)
                    op[1][0] = 1
                else:
                    nums[minindex:minindex + round(midindex1[2] + .1)] = nums1[0:round(midindex1[2] + .1)]
                    nums1 = nums1[round(midindex1[2] + .1):]
                    minindex = minindex + round(midindex1[2] + .1)
                    op[0][0] = 1
            if midindex1[1] == midindex2[1]:
                if op[0][0]==1:
                    nums[maxindex - round(midindex2[2] + .1):maxindex] = nums2[round(midindex2[2] + .51):]
                    nums2 = nums2[:round(midindex2[2] + .51)]
                    maxindex = maxindex - round(midindex2[2] + .1)
                    op[1][1] = 1
                else:
                    nums[maxindex - round(midindex1[2] + .1):maxindex] = nums1[round(midindex1[2] + .51):]
                    nums1 = nums1[:round(midindex1[2] + .51)]
                    maxindex = maxindex - round(midindex1[2] + .1)
                    op[0][1] = 1
            print('nums is:', nums)
            # if minindex>lenAll/2:
            #     break
            # if maxindex<lenAll/2:
            #     break
            if sum(op[0][:]) == 2:
                nums[minindex:maxindex]=nums2
                print('nums is:', nums)
                if lenAll % 2 == 1:
                    return nums[int((lenAll - 1) / 2)]
                else:
                    return (nums[int(lenAll / 2 - 1)] + nums[int(lenAll / 2)]) / 2

            if sum(op[1][:]) == 2:
                nums[minindex:maxindex] = nums1
                print('nums is:', nums)
                if lenAll % 2 == 1:
                    return nums[int((lenAll - 1) / 2)]
                else:
                    return (nums[int(lenAll / 2 - 1)] + nums[int(lenAll / 2)]) / 2

            midindex1 = findMedianSortedArrays3(nums1)
            midindex2 = findMedianSortedArrays3(nums2)
        nums[minindex]=min(nums1+nums2)
        nums[minindex+1] = max(nums1+nums2)
        if lenAll%2==1:
            return nums[int((lenAll - 1) / 2)]
        else:
            return (nums[int(lenAll / 2-1)]+ nums[int(lenAll / 2)])/2

def findMedianSortedArrays3(nums1):
    lens1 = len(nums1)
    if lens1==0:
        return nums1, nums1, None
    else:
        if lens1 % 2 == 1:
            return nums1[int((lens1 - 1) / 2)], nums1[int((lens1 - 1) / 2)], (lens1 - 1)/2
        else:
            return nums1[int(lens1 / 2)-1], nums1[int(lens1 / 2)], (lens1-1)/2
def findMedianSortedArrays2(nums1):
    lens1 = len(nums1)
    if lens1 % 2 == 1:
        return nums1[int((lens1 - 1) / 2)]
    else:
        return (nums1[int(lens1 / 2)-1]+ nums1[int(lens1 / 2)])/2



p = Solution()
# nums1 = [1, 2, 4, 8, 9, 10, 15]
# nums2 = [3, 4, 5, 7, 8, 9, 10, 11, 12, 13]
nums1 = [2,5]
nums2 = [3,4,6]
print(nums1)
print(nums2)
mid=p.findMedianSortedArrays(nums1, nums2)
print(mid)
