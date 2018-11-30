# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 6/20/18
-------------------------------------------------
   File Name：     solution2
   Description :
   Author :       zhaobx
   date：          6/20/18
-------------------------------------------------
   Change Activity:
                   6/20/18:
-------------------------------------------------
"""
# from Cython.Compiler.ExprNodes import ListNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: List
        :type l2: List
        :rtype: List
        """
        num1=0
        num2=0
        i=0
        for num in l1:
            num1 += num*(10**i)
            i+=1
        i=0
        for num in l2:
            num2 += num*10**i
            i+=1
        product = num1+num2
        l3=[]
        while product>0:
            m = product%10
            product=int(product/10)
            l3.append(m)
        return l3

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None: return l2
        if l2==None: return l1
        num1=0
        num2=0
        i=0
        while l1:
            num1 += l1.val*(10**i)
            l1=l1.next
            i+=1
        print(num1)
        i=0
        while l2:
            num2 += l2.val*10**i
            l2=l2.next
            i+=1
        print(num2)
        product = num1+num2
        print(product)
        i=0
        while product>0:
            m = product%10
            product=int(product/10)
            if i==0:
                l3=ListNode(m)
                n=l3
            else:
                n.next=ListNode(m)
                n=n.next
            i+=1
        i = 0
        num3=0
        while l3:
            num3 += l3.val * 10 ** i
            l3 = l3.next
            i += 1
        print(num3)
        return l3

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None: return l2
        if l2==None: return l1
        num1=0
        num2=0
        i=0
        while l1:
            num1 += l1.val*(10**i)
            l1=l1.next
            i+=1
        i=0
        while l2:
            num2 += l2.val*10**i
            l2=l2.next
            i+=1
        product = num1+num2
        i=0
        while product>0:
            m = product%10
            product=int(product/10)
            if i==0:
                l3=ListNode(m)
                n=l3
            else:
                n.next=ListNode(m)
                n=n.next
            i+=1
        return l3

# l1 = [2,4,3]
# l2 = [5,6,4]
p = Solution()
# print(p.addTwoNumbers(l1,l2))

l1 = ListNode(2)
n = l1
n.next = ListNode(4)
n = n.next
n.next = ListNode(3)
n = n.next
print(l1.val, l1.next.val, l1.next.next.val)


l2 = ListNode(5)
n = l2
n.next = ListNode(6)
n = n.next
n.next = ListNode(4)
n = n.next

print(l2.val, l2.next.val, l2.next.next.val)
p.addTwoNumbers2(l1, l2)


