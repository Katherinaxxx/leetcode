#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/12 下午7:56
@Author : Catherinexxx
@Site : 
@File : 75. Sort Colors.py
@Software: PyCharm
"""
"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，
使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
"""
# 计数0,1，2 个数 之后重写 O(n^2)time O(n)space
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         cnt = [0] * 3
#         for n in nums: cnt[n] += 1
#         i = 0
#         for cur in range(3):
#             for j in range(cnt[cur]):
#                 nums[i] = cur
#                 i += 1

# 三指针 O(n)time O(1)space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = cur = 0
        r = len(nums) - 1
        while cur <= r:
            if nums[cur] == 0:
                if cur != l:
                    nums[cur], nums[l] = nums[l], nums[cur]
                cur += 1
                l += 1
            elif nums[cur] == 2:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
            else:
                cur += 1
