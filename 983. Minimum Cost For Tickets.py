#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/6 下午2:38
@Author : Catherinexxx
@Site : 
@File : 983. Minimum Cost For Tickets.py
@Software: PyCharm
"""
'''
在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。

火车票有三种不同的销售方式：

一张为期一天的通行证售价为 costs[0] 美元；
一张为期七天的通行证售价为 costs[1] 美元；
一张为期三十天的通行证售价为 costs[2] 美元。
通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。

返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-cost-for-tickets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# DP 对于本题不难想到应该用一个数组存储到当前某一天需要花费的最少费用，这里为了下标和天数对应，dp数组的长度选择 days 中最后一个天数多加 1 个长度，因为开始没有费用，所以初始化为 0 ，之后开始对 dp 数组进行更新，那么每到达一个位置首先考虑当前天数是否在days 中，如果不在那花费的费用肯定和它前一天花费的最少费用相同(这里用一个 idx 指标指示应该处理哪一个天数，这样就不必用 if i in days 这样的语句判断天数是否需要处理了，可以让程序快一些)，如果在的话，我们就要从三种购买方式中选择一种花费费用最少的，即你想到达第 i 天，你需要从 i 的前1或7或30天的后一位置花费对应cost[0]、cost[1]、cost[2]的钱才能到第 i 天。

# class Solution:
#     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
#         dp = [0] * (days[-1]+1+7+30)
#         for i in range(1,days[-1]+1):
#             if i not in days:
#                 dp[i+37] = dp[i+37-1]
#             else:
#                 dp[i+37] = min(dp[i+37-1]+costs[0], dp[i+37-7]+costs[1], dp[i+37-30]+costs[2])
#         return dp[-1]

# 稍微优化一下 不用在前面加这么多辅助 用max（0,i-1/7/30)即可
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1]+1)
        for i in range(1,days[-1]+1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[max(0,i-1)]+costs[0], dp[max(0,i-7)]+costs[1], dp[max(0,i-30)]+costs[2])
        return dp[-1]