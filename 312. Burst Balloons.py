#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/21 下午3:00
@Author : Catherinexxx
@Site : 
@File : 312. Burst Balloons.py
@Software: PyCharm
"""
"""
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/burst-balloons
著作权
"""


# 递归+回溯 O(n！)超时
# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         cur, self.res = [False] * len(nums), 0
#         def recursion(cur, coin):
#             # 所有气球都破了
#             if all(cur):
#                 self.res = max(coin, self.res)
#                 return
#             for i in range(len(nums)):
#                 if not cur[i]:
#                     # 戳破气球i
#                     cur[i] = True

#                     left, right = 1, 1
#                     if i-1>=0:
#                         for _ in range(i-1,-1,-1):
#                             if not cur[_]:
#                                 left = nums[_]
#                                 break

#                     # left = 1 if i-1<0 or not cur[i-1] else nums[i-1]
#                     # right = 1 if i+1>len(nums)-1 or not cur[i+1] else nums[i+1]

#                     if i+1<=len(nums)-1:
#                         for _ in range(i+1,len(nums)):
#                             if not cur[_]:
#                                 right = nums[_]
#                                 break

#                     coin += left*nums[i]*right
#                     recursion(cur, coin)
#                     # 回溯
#                     cur[i] = False
#                     coin -= left*nums[i]*right
#         recursion(cur, 0)
#         return self.res


# DP 从一个个戳气球 转变为一个个加气球 O(n^3)time O(n^2)space
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # reframe problem as before 增加左右边界
        nums = [1] + nums + [1]
        n = len(nums)

        # dp will store the results of our calls
        # dp[left][right]表示以left right能获得的硬币的最大数目
        dp = [[0] * n for _ in range(n)]

        # iterate over dp and incrementally build up to dp[0][n-1]
        for left in range(n - 2, -1, -1):
            for right in range(left + 2, n):
                # same formula to get the best score from (left, right) as before
                # 前面为增加一个气球的金币数 后面为左右两部分金币数
                dp[left][right] = max(
                    nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right] for i in range(left + 1, right))

        return dp[0][n - 1]  # dp[0][-1]