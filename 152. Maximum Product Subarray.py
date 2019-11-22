#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/13 上午11:57
@Author : Catherinexxx
@Site : 
@File : 152. Maximum Product Subarray.py
@Software: PyCharm
"""

# DP 乘积正负号 因此要保存最大值最小值 负数大小交换
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         imax = 1
#         imin = 1
#         res = float('-inf')
#         n = len(nums)
#         for i in range(n):
#             if(nums[i]<=0):
#                 imax, imin = imin, imax
#             imax = max(imax*nums[i], nums[i])
#             imin = min(imin*nums[i], nums[i])
#             res = max(res, imax)
#         return res

# 国际站
class Solution:
    def maxProduct(self, A):
        B = A[::-1] # 倒序
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)