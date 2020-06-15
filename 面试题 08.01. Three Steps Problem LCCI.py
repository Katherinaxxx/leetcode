#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/25 下午1:58
@Author : Catherinexxx
@Site : 
@File : 面试题 08.01. Three Steps Problem LCCI.py
@Software: PyCharm
"""
'''
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/three-steps-problem-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# DP O(n)time O(1)space
# dp[i]表示上到第i层台阶的方式
# i-1 一步上来（1） i-2 两个一步或者两步（2） i-3 三个一步或两步一步【均变为i-1/i-2不算】或三步（1）
# dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
class Solution:
    def waysToStep(self, n: int) -> int:
        a,b,c=4,2,1
        if n<3:
            return n
        if n==3:
            return 4
        for i in range(n-3):
            a,b,c=(a+b+c)%1000000007,a,b
        return a