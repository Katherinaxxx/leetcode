#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/2/17 下午4:04
@Author : Catherinexxx
@Site : 
@File : LCOF40.py
@Software: PyCharm
"""
# 1.内置函数 sort O(nlogn)

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]

# 2.快排
def partition(input, low, high):
    pivot = input[low]
    while low < high:
        while low < high and pivot <= input[high]:
            high -= 1
        input[low] = input[high]
        while low < high and pivot >= input[low]:
            low += 1
        input[high] = input[low]
    input[low] = pivot
    return low

class Solution(object):
    def getLeastNumbers(self, tinput, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k > len(tinput) or k <= 0: return []
        idx = partition(tinput, 0, len(tinput) - 1)
        low = 0
        high = len(tinput) - 1
        while idx != k - 1:
            if idx < k - 1:
                low = idx + 1
                idx = partition(tinput, low, high)
            if idx > k - 1:
                high = idx - 1
                idx = partition(tinput, low, high)
        return tinput[:k]