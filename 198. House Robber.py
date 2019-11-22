#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/15 下午12:01
@Author : Catherinexxx
@Site : 
@File : 198. House Robber.py
@Software: PyCharm
"""


# DP
# a 重复子问题
#     a[i][0,1]: 0~i能偷到的最大 0不偷 1偷
#         a[i][0] = max(a[i-1][0], a[i-1][1])
#         a[i][1] = a[i-1][0] + nums[i]

# b 定义状态数组
# c DP方程
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a = [[0] * 2 for _ in range(len(nums))]
        a[0][1] = nums[0]

        for i in range(1, len(nums)):
            a[i][0] = max(a[i - 1][0], a[i - 1][1])
            a[i][1] = a[i - 1][0] + nums[i]
        return max(a[-1][0], a[-1][1])


# f(0) = nums[0]
# f(1) = max(num[0], num[1])
# f(k) = max( f(k-2) + nums[k], f(k-1) )
class Solution:

    def rob(self, nums):
        last, now = 0, 0

        for i in nums: last, now = now, max(last + i, now)

        return now