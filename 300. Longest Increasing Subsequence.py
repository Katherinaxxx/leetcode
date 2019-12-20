#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/12/4 上午11:39
@Author : Catherinexxx
@Site : 
@File : 300. Longest Increasing Subsequence.py
@Software: PyCharm
"""


# 1、DP O(n^2)
class Solution:

    # 将 dp 数组定义为：以 nums[i] 结尾的最长上升子序列的长度
    # 那么题目要求的，就是这个 dp 数组中的最大者
    # 以数组  [10, 9, 2, 5, 3, 7, 101, 18] 为例
    # dp 的值： 1  1  1  2  2  3  4    4

    def lengthOfLIS(self, nums):
        size = len(nums)
        # 特判
        if size <= 1:
            return size

        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    # + 1 的位置不要加错了
                    dp[i] = max(dp[i], dp[j] + 1)
        # 最后要全部一看遍，取最大值
        return max(dp)


# 2、binary search O(nlogn) 不太好想诶
class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size