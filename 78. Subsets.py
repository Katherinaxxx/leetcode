#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/30 下午2:51
@Author : Catherinexxx
@Site : 
@File : 78. Subsets.py
@Software: PyCharm
"""
'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。
'''


# 迭代
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res += [[i] + a for a in res]
        return res


# 递归
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)

#         def helper(i, tmp):
#             res.append(tmp)
#             for j in range(i, n):
#                 helper(j + 1,tmp + [nums[j]] )
#         helper(0, [])
#         return res
s