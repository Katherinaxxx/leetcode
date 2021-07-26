#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/5/23 2:50 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面.py
@Description: 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
"""
# 遍历 O(n) O(n)
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        q_list,o_list = [],[]
        for i in nums:
            if i%2==1:
                q_list.append(i)
            else:
                o_list.append(i)
        return q_list+o_list
# 双指针 一个从前往后 一个从后往前
# O(n) time O(1) space
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] % 2 == 0:
                if nums[j] % 2 == 1: # 左右刚好反了 交换位置
                    nums[i], nums[j] = nums[j], nums[i]
                else: # 左偶 右偶(右边这个不用变)
                    j -= 1
            else:
                i += 1

        return nums