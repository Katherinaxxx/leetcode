#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/25 下午8:55
@Author : Catherinexxx
@Site : 
@File : 排序.py
@Software: PyCharm
"""
"""
https://www.cnblogs.com/Mufasa/p/10527387.html
"""
before = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
after = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]
# 冒泡 前后比较 交换位置 - O(n^2) O(1)
def buble(l):
    while True:
        flag = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                flag = True
        if not flag:
            break
    return l
# print(buble(before)==after)

# 选择 选出后面最小的 交换位置 - O(n^2) O(1)
def select(l):
    for i in range(len(l)-1):
        index = i
        for j in range(i+1, len(l)):
            if l[j]<l[index]:
                index = j
        if index != i:
            l[i], l[index] = l[index], l[i]
    return l
# print(select(before)==after)

# 插入 插入到前面有序的位置中 O(n^2)
def insert_sort(d):   # 直接插入排序，因为要用到后面的希尔排序，所以转成function
     d1 = [d[0]]
     for i in d[1:]:
         state = 1
         for j in range(len(d1) - 1, -1, -1):
             if i >= d1[j]:
                 d1.insert(j + 1, i)  # 将元素插入数组
                 state = 0
                 break
         if state:
             d1.insert(0, i)
     return d1
# print(insert_sort(before)==after)

# shell 【从大范围到小范围进行比较-交换】类似冒泡和插入的联合
def shellSort(arr):
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n // 2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(gap, n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

                # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2
    return arr
print(shellSort(before)==after)


# 归并 分两遍 再融合 O(nlogn) O(n)
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    # Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

# 快排 选一个pivot 小于他的放左边 大于的放右边 O(nlogn) O(n)
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

quickSort(before,0,len(before)-1)