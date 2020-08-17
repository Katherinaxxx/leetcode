#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/15 下午2:54
@Author : Catherinexxx
@Site : 
@File : 美团2019时间内考试最高得分.py
@Software: PyCharm
"""

"""
链接：https://www.nowcoder.com/questionTerminal/a1792d443f914f2b928d2a157cd7900d
来源：牛客网

小明同学在参加一场考试，考试时间2个小时。试卷上一共有n道题目，小明要在规定时间内，完成一定数量的题目。  考试中不限制试题作答顺序，对于 i 第道题目，小明有三种不同的策略可以选择:  (1)直接跳过这道题目，不花费时间，本题得0分。

(2)只做一部分题目，花费pi分钟的时间，本题可以得到ai分。  (3)做完整个题目，花费qi分钟的时间，本题可以得到bi分。 

小明想知道，他最多能得到多少分。
"""

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
time_limit = 120
dp = [0] * (time_limit + 1)
for i in range(1, n + 1):
    for j in range(time_limit, 0, -1):
        p, a, q, b = data[i - 1]
        if j >= q:
            dp[j] = max(dp[j], dp[j-p] + a, dp[j-q] + b)
        elif j >= p:
            dp[j] = max(dp[j], dp[j-p] + a)
print(dp[-1])

l=[[2,4],[1,0]]
l.sort()

beijing nanjing
nanjing guangzhou
guangzhou shanghai
shanghai beijing
fuzhou beijing
beijing fuzhou