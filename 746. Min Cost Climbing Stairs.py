#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/24 下午12:33
@Author : Catherinexxx
@Site : 
@File : 746. Min Cost Climbing Stairs.py
@Software: PyCharm
"""
"""
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# dp[i]表示爬到第i个台阶最低的花费
# dp[0] = cost[0] dp[1] = cost[1]
# 可以爬一阶或者两阶 dp[i] = min(dp[i-1], dp[i-2])+cost[i] 只需看到i-1阶
# 最后一步 如果是从倒数第二层爬两步（肯定比一步少）则不用加cost[-1] 如果是从倒数爬两步 则要加cost[-1] 返回这二者最小值即可
# O(n)time O(n)space
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         if len(cost) == 2:
#             return min(cost)
#         dp = [0] * (len(cost)-1)
#         dp[0] = cost[0]
#         dp[1] = cost[1]
#         for i in range(2, len(cost)-1):
#             dp[i] = min(dp[i-1], dp[i-2])+cost[i]
#         return min(dp[-2]+cost[-1], dp[-1])

# 优化DP空间
# O(n)time O(1)space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        dp = [cost[0], cost[1]]
        for i in range(2, len(cost)-1):
            dp[1], dp[0] = min(dp[1], dp[0])+cost[i], dp[1]
        return min(dp[0]+cost[-1], dp[1])