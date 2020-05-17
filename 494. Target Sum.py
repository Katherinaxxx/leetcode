#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/17 下午3:21
@Author : Catherinexxx
@Site : 
@File : 494. Target Sum.py
@Software: PyCharm
"""
"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 树 递归 O(2^n)time超时
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         self.res = 0
#         def helper(i, s):
#             if i == len(nums)-1 and S == s:
#                 self.res += 1
#                 return
#             if i == len(nums)-1 and S != s:
#                 return
#             helper(i+1, s+nums[i])
#             helper(i+1, s-nums[i])
#         helper(-1, 0)
#         return self.res

# 优化 dfs
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        import functools

        @functools.lru_cache(None)
        def dfs(i, S):
            if i == len(nums): return [0, 1][S == 0]  # 这种写法学到了
            return dfs(i + 1, S - nums[i]) + dfs(i + 1, S + nums[i])

        return dfs(0, S)


# DP 背包问题 dp[i][j]表示用前i个和为j的方案数目  dp[-1][S]
# dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j+nums[i]]
# O(nm) time  O(m)space
class Solution:
    def findTargetSumWays(self, nums, S):
        length, dp = len(nums), {(-1, 0): 1}
        for i in range(0, length):
            for j in range(-sum(nums), sum(nums) + 1):
                dp[(i, j)] = dp.get((i - 1, j - nums[i]), 0) + dp.get((i - 1, j + nums[i]), 0)
        return dp.get((length - 1, S), 0)