#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/15 下午12:01
@Author : Catherinexxx
@Site : 
@File : 198. House Robber.py
@Software: PyCharm
"""


# DP
# a 重复子问题
#     a[i][0,1]: 0~i能偷到的最大 0不偷 1偷
#         a[i][0] = max(a[i-1][0], a[i-1][1])
#         a[i][1] = a[i-1][0] + nums[i]

# b 定义状态数组
# c DP方程
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a = [[0] * 2 for _ in range(len(nums))]
        a[0][1] = nums[0]

        for i in range(1, len(nums)):
            a[i][0] = max(a[i - 1][0], a[i - 1][1])
            a[i][1] = a[i - 1][0] + nums[i]
        return max(a[-1][0], a[-1][1])


# dp 不能抢相邻的 dp[i][0,1]表示到第i家偷窃到的最高金额
# dp[i]] = max(dp[i-1], dp[i-2][0] + nums[i])
#  O(n)time O(n)space
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [ 0 for _ in range(len(nums))] #预生成等长的dp数组
        if len(dp) <= 0:
            return 0 #没有人家，没有钱
        if len(dp) >= 1:
            dp[0] = nums[0]  #只有一家的时候，没得选，就它了
        if len(dp) >= 2:
            dp[1] = max(nums[1],dp[0]) #这里写成 max(num[1],num[0]) 亦可，但是为了更通用。我们这样子写。表示要么打劫当前这一家，要么打劫前一家
        for i in range(2,len(nums)):
            dp[i] = max(nums[i] + dp[i-2],dp[i-1]) # 这个加 dp[i-2] 是最精髓的，表示打劫当前这家，并且寻找打劫上上一家的最大值，做累加
        # print(dp)  #个人调试用，显示dp数组。发现上面还是改成大于等于比较好。不然第一项和第二项始终为0。数据失真
        return dp[-1] #返回最后一项，也就是基于当前数据的最大收益


# f(0) = nums[0]
# f(1) = max(num[0], num[1])
# f(k) = max( f(k-2) + nums[k], f(k-1) )
# 秀 O(n)time O(1)space
class Solution:

    def rob(self, nums):
        last, now = 0, 0

        for i in nums: last, now = now, max(last + i, now)

        return now