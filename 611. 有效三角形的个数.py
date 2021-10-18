#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/8/4 10:55 PM
@Author : Catherinexxx
@File : 611. 有效三角形的个数.py
@Description: 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
"""
# 排序+双指针
# 两边之和大于第三边->只要最长的边小于另外两边之和 则是个有效的三角形
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-1, 1, -1):
            l, r = 0, i-1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    # nums[r] 和 nums[l:r-1] 和 nums[i]都可以组成三角形
                    res += (r-1) - l + 1
                    r -= 1
                else:
                    # 不够大了 所以l要往后移
                    l += 1
        return res
