# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 12/1/18
-------------------------------------------------
   File Name：     chainTest
   Description :
   Author :       zhaobx
   date：          12/1/18
-------------------------------------------------
   Change Activity:
                   12/1/18:
-------------------------------------------------
"""
class Node(object):
    def __init__(self, val, p):
        self.data = val
        self.next = p

class LinkList(object):
    def __init__(self):
        # self.head - 0
        self.head = 0

    def __getitem__(self, key):
        if self.is_isempty():
            print('linklist is empty')
            return
        elif key < 0 or key > self.getlength():
            print('the given key is error')
            return
        else:
            return self.getitem(key)

    def __setitem__(self, key, value):

        if self.is_empty():
            print('linklist is empty!')
            return
        elif key < 0 or key > self.getlength():
            print('the given key is error')
            return
        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self, data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):
        p = self.head
        length = 0
        while p != 0:
            length += 1
            p = p.next

        return length

    def is_empty(self):

        if self.getlength() == 0:
            return True
        else:
            return False

    def clear(self):
        self.head = 0

    def append(self, item):
        q = Node(item)
        if self.head == 0:
            self.head = q
        else:
            p = self.head
            while p.next != 0:
                p = p.next
            p.next = q
    def getitem(self, index):
        if self.is_empty():
            print('Linklist is empty')
            return

        j = 0
        p = self.head

        while p.next != 0 and j < index:
            p = p.next
            j += 1
        if j == index:
            return p.data
        else:
            print('target is not exist!')

    def insert(self, index, item):
        if self.is_empty() or index < 0 or index > self.getlength():
            print('Linklist is empty')
            return

        if index == 0:
            # q = self.head
            # q.data = item
            q = Node(item, self.head)

            self.head = q

        j = 0
        p = self.head
        post = self.head
        while p.next != 0 and j < index:
            post = p
            p = p.next
            j += 1

        if j == index:
            q = Node(item, p)
            post.next = q
            q.next = p
            return p.data
        # else:
        #     print('target is not exist!')

    def delete(self, index):
        if self.is_empty() or index < 0 or index > self.getlength():
            print('Linklist is empyt or .....')
            return

        if index == 0:
            # self.head = self.head.next
            q = self.head
            self.head = q.next
            return

        c = self.head
        p = c
        j = 0
        while p != 0 and j < index:
            p = c
            c = c.next
            j = j + 1

        p.next = c.next

    def index(self, value):
        if self.is_empty():
            print('empty linklist, please check')
            return -1

        p = self.head
        i = 0
        while p != 0:
            if p.data == value:
                return i
                break
            else:
                i += 1
                p = p.next
        else:
            return -1
# class NodeBidirectional
# class Linklist(object):


i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    else:
        i += 1
else:
    print('else output')