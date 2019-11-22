#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/13 上午11:23
@Author : Catherinexxx
@Site : 
@File : 53. Maximum Subarray.py
@Software: PyCharm
"""
# dp 超时
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         res = max(nums)
#         dp = nums
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 dp[j] += nums[i]
#             tmp = max(dp)
#             res = max(res, tmp)
#         return res
# dp 正增益 负则取下一个
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=0
        res=nums[0]
        n=len(nums)
        for i in range(n):
            # cur_sum = cur_sum + nums[i] if cur_sum>0 else nums[i]
            if(cur_sum>0):
                cur_sum+=nums[i]
            else:
                cur_sum=nums[i]
            res=max(res,cur_sum)
        return res


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], ) + nums[i]

            nums[i] = max(nums[i - 1], 0) + nums[i]
        return max(nums)