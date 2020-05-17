#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/16 下午2:14
@Author : Catherinexxx
@Site : 
@File : 416. Partition Equal Subset Sum.py
@Software: PyCharm
"""
"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
"""

# DP
# 和为偶数则继续，否则false
# 接下来只需找出一部分数的和 ?= target(sum>>1)
# dp[i][j]表示[0,i]一些数的和是否等于j
# 最后返回dp[len(nums)-1][target]
# O(nm)time O(nm)space m=sum/2
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s >> 1
        # define dp
        dp = [[False]*(target+1) for _ in range(len(nums))]
        dp[0][0] = True
        for i in range(len(nums)):
            for j in range(1, target+1):
                # 下标
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                elif j == nums[i]:
                    dp[i][j] = True
                else:
                    # 选或不选
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[-1][-1]

# 优化DP 逆序
class Solution(object):
    def canPartition(self, nums):
        sums=sum(nums)
        if sums%2==1:
            return False
        target=sums//2

        dp=[False for _ in range(target+1)]
        dp[0]=True

        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j]=dp[j] or dp[j-nums[i]]
        return dp[-1]