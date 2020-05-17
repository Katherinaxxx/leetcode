#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/12 下午9:27
@Author : Catherinexxx
@Site : 
@File : 309. Best Time to Buy and Sell Stock with Cooldown.py
@Software: PyCharm
"""
"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 再次看了一个套路解股票系列 dp[i][k][0,1] 再分别分析持有不持有的原因（以前状态的选择）
# dp[i][0,1]-第i天最大利润
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])


# DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices) + 2)]
        dp[1][1] = float("-inf")
        for i in range(2, len(prices) + 2):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i - 2])
        return dp[-1][0]
