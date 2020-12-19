#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/16 下午12:09
@Author : Catherinexxx
@Site : 
@File : move-zeros.py
@Software: PyCharm
"""

# python


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j += 1


# 双指针 i遇0 则j从j后找到第一个不为0的 交换 然后i=j j继续往后找
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            j = i + 1
            while j < len(nums) and nums[j] == 0:
                j += 1
            if i < len(nums) and j < len(nums):
                nums[i], nums[j] = nums[j], nums[i]


# // java
# class Solution {
#     public void moveZeroes(int[] nums) {
#         int j = 0;
#         for (int i = 0; i < nums.length; ++i) {
#             if (nums[i] != 0) {
#                 nums[j] = nums[i];
#                 if (i != j) {
#                     nums[i] = 0;
#                 }
#                 j++;
#             }
#         }
#     }
# }