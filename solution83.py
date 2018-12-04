# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 12/4/18
-------------------------------------------------
   File Name：     solution83
   Description :
   Author :       zhaobx
   date：          12/4/18
-------------------------------------------------
   Change Activity:
                   12/4/18:
-------------------------------------------------
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        if head.next == None:
            return head
        pre = head
        cur = head.next
        while cur:

            if pre.val == cur.val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return head
    def info(self,head):
        while(head):
            print(head.val, end='->')
            head = head.next
        print()

head = ListNode(1)
q = ListNode(1)
head.next = q
p = ListNode(2)
q.next = p
q = p
p = ListNode(2)
q.next = p
q = p
p = ListNode(3)
q.next = p
q = p
p = ListNode(3)
q.next = p
q = p
s = Solution()
s.info(head)
s.deleteDuplicates(head)
s.info(head)

