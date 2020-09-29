#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/9/12 下午5:06
@Author : Catherinexxx
@Site : 
@File : LCOF62. 圆圈中最后剩下的数字.py
@Software: PyCharm
"""
"""
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

题解：
https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-by-lee/
"""

# 递归 O(n) O(n)
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return self.f(n,m)
    def f(self, n, m):
        if n == 0:
            return 0
        x = self.f(n-1, m)
        return (m+x)%n

# 迭代 O(n) O(1)
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f
