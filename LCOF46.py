#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/2/18 下午3:45
@Author : Catherinexxx
@Site : 
@File : LCOF46.py
@Software: PyCharm
"""
# dp
# dp[n] = dp[n-1] num[n-1:n+1]>25
# dp[n] = dp[n-2] + dp[n-1]

class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        dp = [1] + [0]*len(num)
        for i in range(len(num)):
            # 不能合成一个
            if i==0 or int(num[i-1:i+1]) > 25 or num[i-1] == '0' :
                dp[i+1] = dp[i]
            # 可以合成一个
            else:
                dp[i+1] = dp[i] + dp[i-1]
        return dp[-1]

print(Solution().translateNum(205))