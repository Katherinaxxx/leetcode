#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/25 下午7:16
@Author : Catherinexxx
@Site : 
@File : 完美世界2020秋招.py
@Software: PyCharm
"""
# 反序数字
s = input()
s = s.split()[::-1]
print(' '.join(s))

# 魔方比赛 83ac
n = int(input())
score = list(map(int, input().split()))
time = list(map(int, input().split()))
time_limit = int(input())
dp = [0] * (time_limit + 1)
for i in range(1, n + 1):
    for j in range(time_limit, 0, -1):
        if j >= time[i-1]:
            dp[j] = max(dp[j], dp[j-time[i-1]] + score[i-1])
print(dp[-1])

# 面试官数量 73ac
n = int(input())
arrive = list(map(int, input().split()))
leave = list(map(int, input().split()))

res = 1
s = [leave[0]]
avail = 0

def shell(l):
    gap = len(l)
    while gap > 1:
        for i in range(gap, len(l)):
            for j in range(i%gap, i, gap):
                if l[i] < l[j]:
                    l[i], l[j] = l[j], l[i]
    return l
for i in range(1, n):
    while s and s[0]<=arrive[i]: # shifang
        s.pop(0)
        avail += 1

    if avail == 0:
        res += 1
    elif avail > 0:
        avail -= 1
    s.append(leave[i])
    s=shell(s)
print(res)

