#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/9/22 下午10:34
@Author : Catherinexxx
@Site : 
@File : LCOF51数组中的逆序对.py
@Software: PyCharm
"""


# 暴力 两两对比 O(n^2)
# stack 超时
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 1 if nums[0] > nums[1] else 0
        stack = []
        res = 0
        i = 0
        while nums:
            if not stack:
                stack.append(nums.pop(0))
            else:
                tmp_stack = []
                while stack and nums[0] >= stack[-1]:
                    tmp = stack.pop()
                    tmp_stack.append(tmp)
                res += len(stack)
                stack.append(nums.pop(0))
                for tmp in tmp_stack[::-1]:
                    stack.append(tmp)
        return res


# 归并排序 merge的过程中 计算数目 O(nlogn) O(n)
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0

        def merge(nums, start, mid, end):
            i, j, temp = start, mid + 1, []
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    # 计算逆序对
                    self.cnt += mid - i + 1
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1

            for i in range(len(temp)):
                nums[start + i] = temp[i]
            # nums[low : high+1] = temp

        def mergeSort(nums, start, end):
            if start >= end: return
            mid = (start + end) >> 1
            mergeSort(nums, start, mid)
            mergeSort(nums, mid + 1, end)
            merge(nums, start, mid, end)

        mergeSort(nums, 0, len(nums) - 1)
        return self.cnt