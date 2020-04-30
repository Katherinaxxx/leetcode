#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/30 下午5:04
@Author : Catherinexxx
@Site : 
@File : 338. Counting Bits.py
@Software: PyCharm
"""
'''
给定一个非负整数 num。
对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
'''

# 库函数 O(n*sizeof(integer)) time
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            res.append(bin(i).count('1'))
        return res

# 本题主要考察二进制的自身特性。
# 二进制的两个特性：
# 奇数的二进制中1的个数=它上一位偶数的二进制中1的个数+1
# 偶数中二进制1的个数等于这个偶数除以2后的数二进制1的个数。

class Solution:
    def countBits(self, num: int) -> List[int]:
        dp=[0]*(num+1)
        for i in range(1,num+1):
            if(i%2==1):
                dp[i]=dp[i-1]+1
            else:
                dp[i]=dp[i//2]
        return dp
