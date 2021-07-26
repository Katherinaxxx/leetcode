#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/5/25 10:29 AM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 剑指 Offer 63. 股票的最大利润.py
@Description: 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
"""
# 维护一个单调栈 O(n) O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        s = []
        ans = float("-inf")
        for x in prices:
            if not s:
                s.append(x)
            elif x > s[-1]:
                s.append(x)
            elif x < s[0]:
                ans = max(ans, s[-1] - s[0])
                s = [x]
        ans = max(ans, s[-1] - s[0])
        return ans

# 遍历一次 维护历史最低点 O(n) O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        min_p = float("inf")
        ans = 0
        for x in prices:
            if x < min_p:
                min_p = x
            ans = max(x-min_p, ans)
        return ans