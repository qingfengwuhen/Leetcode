# -*- coding: utf-8 -*-
"""
Created by Zhao Baoxin on 11/30/18
-------------------------------------------------
   File Name：     sortMethods
   Description :
   Author :       zhaobx
   date：          11/30/18
-------------------------------------------------
   Change Activity:
                   11/30/18:
-------------------------------------------------
"""
from datetime import *
import time
import copy

def insert_sort2(ilist):
    start = time.time()
    for i in range(len(ilist)):
        for j in range(len(ilist)):
            if ilist[i] < ilist[j]:
                ilist.insert(j, ilist.pop(i))
                break
    end = time.time()
    print(end - start)
    return ilist

def insert_sort(ilist):
    start = time.time()
    for i in range(1, len(ilist)):
        for j in range(len(ilist)):
            if ilist[i] < ilist[j] and i > j:
                ilist.insert(j, ilist.pop(i))
                break
    end = time.time()
    print(end - start)
    return ilist

def shell_sort(slist):
    start = time.time()
    gap = len(slist)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(slist)):
            for j in range(i % gap, i, gap):
                if slist[i] < slist[j]:
                    slist[i], slist[j] = slist[j], slist[i]
    end = time.time()
    print(end-start)
    return slist

def bubble_sort(blist):
    start = time.time()
    for i in range(len(blist)):
        for j in range(i+1, len(blist)):
            if blist[i] > blist[j]:
                blist[i], blist[j] = blist[j], blist[i]
    end = time.time()
    print(end-start)
    return blist

def quick_sort(qlist):
    # start = time.time()
    if qlist==[]:
        return []
    else:
        qfirst = qlist[0]
        qless = quick_sort([l for l in qlist[1:] if l < qfirst])
        qmore = quick_sort([m for m in qlist[1:] if m >= qfirst])
        # end=time.time()
        # print(end-start)
        return qless + [qfirst] + qmore

def select_sort(slist):
    for i in range(len(slist)):
        x = i
        for j in range(i, len(slist)):
            if slist[j] < slist[x]:
                x=j
        slist[i], slist[x] = slist[x], slist[i]
    return slist

def heap_sort2(hlist):
    def heap_adjust(parent):
        child = 2 * parent + 1
        while child < len(heap):
            if child + 1 < len(heap): # if there exists right child
                if heap[child + 1] > heap[child]: # find the maximal child
                    child += 1
            if heap[parent] >= heap[child]: # change the position (one time is enough)
                break
            heap[parent], heap[child] = heap[child], heap[parent]
            parent, child = child, 2 * child + 1
            # else:
            #     if heap[parent] >= heap[child]:
            #         break
            #     else:
            #         heap[parent], heap[child] = heap[child], heap[parent]
    heap, hlist = copy.copy(hlist), []
    for i in range(len(heap) // 2, -1, -1):
        heap_adjust(i)
    while len(heap) != 0:
        heap[0], heap[-1] = heap[-1], heap[0]
        hlist.insert(0, heap.pop())
        heap_adjust(0)
    return hlist

def heap_sort(hlist):
    def heap_adjust(parent):
        child = 2 * parent + 1  # left child
        while child < len(heap):
            if child + 1 < len(heap):
                if heap[child + 1] > heap[child]:
                    child += 1  # right child
            if heap[parent] >= heap[child]:
                break
            heap[parent], heap[child] = heap[child], heap[parent]
            parent, child = child, 2 * child + 1

    heap, hlist = copy.copy(hlist), []
    for i in range(len(heap) // 2, -1, -1):
        heap_adjust(i)
    while len(heap) != 0:
        heap[0], heap[-1] = heap[-1], heap[0]
        hlist.insert(0, heap.pop())
        heap_adjust(0)
    return hlist

def radix_sort(array):
    bucket, digit = [[]], 0
    while len(bucket[0]) != len(array):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(array)):
            num = (array[i] // 10 ** digit) % 10
            bucket[num].append(array[i])
        array.clear()
        for i in range(len(bucket)):
            array += bucket[i]
        digit += 1
    return array

def merge_sort(array):
    def merge_arr(arr_l, arr_r):
        array = []
        while len(arr_l) and len(arr_r):
            if arr_l[0] <= arr_r[0]:
                array.append(arr_l.pop(0))
            elif arr_l[0] > arr_r[0]:
                array.append(arr_r.pop(0))
        if len(arr_l) != 0:
            array += arr_l
        elif len(arr_r) != 0:
            array += arr_r
        return array

    def recursive(array):
        if len(array) == 1:
            return array
        mid = len(array) // 2
        arr_l = recursive(array[:mid])
        arr_r = recursive(array[mid:])
        return merge_arr(arr_l, arr_r)
    return recursive(array)


ilist = [5, 4, 6, 7, 3, 2, 6, 9, 8]
print('ilist is :', ilist)
ilist = insert_sort(ilist)
print('after insert sorting, ilist is :', ilist)
ilist = [5, 4, 6, 7, 3, 2, 6, 9, 8]
# print('ilist is :', ilist)
ilist = insert_sort2(ilist)
print('after insert sorting 2, ilist is :', ilist)

ilist = [5, 4, 6, 7, 3, 2, 6, 9, 8]
# print('ilist is :', ilist)
ilist = shell_sort(ilist)
print('after shell sorting, ilist is :', ilist)

ilist = [5, 4, 6, 7, 3, 2, 6, 9, 8]
# print('ilist is :', ilist)
ilist = bubble_sort(ilist)
print('after bubble sorting, ilist is :', ilist)

ilist = [5, 4, 6, 7, 3, 2, 6, 9, 8]
# print('ilist is :', ilist)
start=time.time()
ilist = quick_sort(ilist)
print(time.time()-start)
print('after quick sorting, ilist is :', ilist)

ilist = [5, 4, 6, 7, 3, 2, 6, 9, 8]
# print('ilist is :', ilist)
ilist = select_sort(ilist)
print('after select sorting, ilist is :', ilist)

ilist = [5, 4, 6, 7, 3, 2, 6, 8, 9]
# print('ilist is :', ilist)
ilist = heap_sort(ilist)
print('after heap sorting, ilist is :', ilist)

ilist = [75, 445, 666, 777, 223, 332, 644, 358, 789, 23, 1123]
# print('ilist is :', ilist)
ilist = radix_sort(ilist)
print('after radix sorting, ilist is :', ilist)

ilist = [75, 445, 666, 777, 223, 332, 644, 358, 789, 23, 1123]
# print('ilist is :', ilist)
ilist = merge_sort(ilist)
print('after merge sorting, ilist is :', ilist)
