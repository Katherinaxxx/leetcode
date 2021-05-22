#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/5/5 5:48 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 740. 删除并获得点数.py
@Description: 给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-and-earn
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# dp
# 转化成打家劫舍
from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m = max(nums)
        d = Counter(nums)
        dp = [0] * (m+1)
        for k in d:
            dp[k] = k * d[k]
        # [2,2,3,4] -> [0,0,2,1,1]
        for i in range(2, m+1):
            dp[i] = max(dp[i-1], dp[i-2]+dp[i])
        return dp[-1]

