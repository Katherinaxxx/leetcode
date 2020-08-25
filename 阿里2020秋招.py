#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/17 下午6:52
@Author : Catherinexxx
@Site : 
@File : 阿里2020秋招.py
@Software: PyCharm
"""

# 完美对 前后两数做差互为相反数

n, k = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(n)]

def helper(x, y):
    i = 1
    s = x[0] + y[0]
    while i < k:
        if x[i] + y[i] != s:
            return False
        i += 1
    return True

def solution():
    res = 0
    for i in range(n-1):
        for j in range(i, n):
            if helper(data[i],data[j]):
                res += 1
    return res

print(solution())

# 二叉树 dp[j][i] =(dp[j][i]%mod+ dp[k][i-1] * dp[j-k-1][i-1]%mod)%mod;
n, m = list(map(int, input().split()))


def solution():
    res = 0

    def recursion(cur_n, depth, l,r,left, right, ):
        nonlocal res
        if cur_n == n and depth == m:
            res += 1
            return
        elif cur_n == n or depth > m or n - cur_n + depth < m:
            return

        if (not left and not right) :
            recursion(cur_n + 1, depth + 1, left=True, right=False)
            recursion(cur_n + 1, depth + 1, left=False, right=True)
        elif left and not right:
            recursion(cur_n + 1, depth + 1, left=True, right=False)
            recursion(cur_n + 1, depth, left=True, right=True)
        else:
            recursion(cur_n + 1, depth + 1, left=False, right=True)

    recursion(cur_n=0, depth=0, left=False, right=False)
    return res


print(solution())


