#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/6 下午2:08
@Author : Catherinexxx
@Site : 
@File : 47. Permutations II.py
@Software: PyCharm
"""

class Solution:
    def permuteUnique(self, nums):
        if len(nums) == 0:
            return []

        # 首先排序，之后才有可能发现重复分支，升序、倒序均可
        nums.sort()
        # nums.sort(reverse=True)

        used = [False] * len(nums)
        res = []
        self.__dfs(nums, 0, [], used, res)
        return res

    def __dfs(self, nums, index, pre, used, res):
        if index == len(nums):
            res.append(pre.copy())
            return
        for i in range(len(nums)):
            if not used[i]:
                # 因为排序以后重复的数一定不会出现在开始，故 i > 0
                # 和之前的数相等，并且之前的数还未使用过，只有出现这种情况，才会出现相同分支
                # 这种情况跳过即可
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                pre.append(nums[i])
                self.__dfs(nums, index + 1, pre, used, res)
                # 回溯
                used[i] = False
                pre.pop()
