#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/29 下午4:22
@Author : Catherinexxx
@Site : 
@File : 121. Best Time to Buy and Sell Stock.py
@Software: PyCharm
"""
'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 两层循环 O(n^2) 超时
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = 0
#         for i in range(len(prices)-1):
#             for j in range(i, len(prices)):
#                 if prices[i] < prices[j]:
#                     res = max(prices[j] - prices[i], res)
#         return res


# DP 最大利润=max（截止前一天最大利润，今天股价-最小股价） o(n) o(n)
# dp[i] = max(dp[i-1], prices[i]-min_price)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * (len(prices) + 1)  # 前面加一个辅助
        min_price = float("inf")

        for i, p in enumerate(prices):
            min_price = min(min_price, p)
            dp[i + 1] = max(dp[i], p - min_price)  # 加了个辅助所以是i+1

        return dp[-1]
