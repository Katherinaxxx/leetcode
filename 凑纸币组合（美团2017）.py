#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/13 下午11:05
@Author : Catherinexxx
@Site : 
@File : 凑纸币组合（美团2017）.py
@Software: PyCharm
"""
"""
给你六种面额 1、5、10、20、50、100 元的纸币，假设每种币值的数量都足够多，编写程序求组成N元（N为0~10000的非负整数）的不同组合的个数。 
"""

"""
使用前i+1种钱币表示总面值为j的方案数=使用前i种钱币表示面值为j的方案数   +   使用前i+1中钱币表示面值为j-coin[i]的方案数
:param n:
:return:
"""

n = int(raw_input())
c = [1, 5, 10, 20, 50, 100]
methods = [[0 for i in range(n + 1)] for j in range(6)]
for i in range(6):
    methods[i][0] = 1
for j in range(n + 1):
    methods[0][j] = 1
for i in range(1, 6):
    for j in range(1, n + 1):
        if j >= c[i]: """这里是指在使用前i种钱币时，只有j>=第i种钱币时，使用前i种钱币找j元钱的方法methods[i][j]才会改变,否则和使用前i-1种钱币组成j元钱的方法相同"""
        methods[i][j] = methods[i - 1][j] + methods[i][j - c[i]]
    else:
        methods[i][j] = methods[i - 1][j]


print
methods[5][n]



n = int(raw_input())
nums = [0 for i in range(n+1)]
coins = [1,5,10,20,50,100]
nums[0]=1
for coin in coins:
    for j in range(coin,n+1):
        nums[j] = nums[j]+nums[j-coin]
print(nums[n])