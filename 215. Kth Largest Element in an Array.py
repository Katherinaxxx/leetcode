#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/11 下午9:12
@Author : Catherinexxx
@Site : 
@File : 215. Kth Largest Element in an Array.py
@Software: PyCharm
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums) - k]


# 快拍
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            pivot = nums[left]
            l = left + 1
            r = right
            while l <= r:
                if nums[l] < pivot and nums[r] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                if nums[l] >= pivot:
                    l += 1
                if nums[r] <= pivot:
                    r -= 1
            nums[r], nums[left] = nums[left], nums[r]
            return r

        left = 0
        right = len(nums) - 1
        while 1:
            idx = partition(left, right)
            if idx == k - 1:
                return nums[idx]
            if idx < k - 1:
                left = idx + 1
            if idx > k - 1:
                right = idx - 1