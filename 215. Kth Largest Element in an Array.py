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

# 堆排序
class Solution:

    def findKthLargest(self, nums, k: int) -> int:
        """堆排序思想"""

        def heapify(a, start, end):
            """ 自上向下堆化
            Args:
                a (list): 输入数组
                start (int): 堆化目标在数组的位置
                end (int): 堆在数组的截止位置
            """
            while True:
                max_pos = start #初始化最大值所在位置为目标所在
                if start*2 + 1 <= end and a[start] < a[start*2+1]:
                    # 如果左叶子节点存在，且大于目标值，则将最大值所在位置指向该节点所在位置
                    max_pos = start*2 + 1
                if start*2 + 2 <= end and a[max_pos] < a[start*2+2]:
                    # 如果右叶子节点存在，且大于目标值，则将最大值所在位置指向该节点所在位置
                    max_pos = start*2 + 2
                if max_pos == start:
                    # 如果目标即为最大，完成该节点堆化，跳出循环
                    break
                # 交换位置，将最大值
                a[start], a[max_pos] = a[max_pos], a[start]
                start = max_pos

        # 建堆,只需要对前半节点堆化
        for i in range(len(nums)//2-1, -1, -1):
            heapify(nums, i, len(nums)-1)
        # 排序，只需要循环K次，排序TOP K个节点
        i = len(nums) - 1
        while i > len(nums) - 1 - k:
            nums[0], nums[i] = nums[i], nums[0]
            i -= 1
            heapify(nums, 0, i)
        return nums[len(nums)-k]

