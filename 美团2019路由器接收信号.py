#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/15 下午3:16
@Author : Catherinexxx
@Site : 
@File : 美团2019路由器接收信号.py
@Software: PyCharm
"""

"""
一条直线上等距离放置了n台路由器。路由器自左向右从1到n编号。第i台路由器到第j台路由器的距离为| i-j |。  每台路由器都有自己的信号强度，第i台路由器的信号强度为ai。所有与第i台路由器距离不超过ai的路由器可以收到第i台路由器的信号（注意，每台路由器都能收到自己的信号）。问一共有多少台路由器可以收到至少k台不同路由器的信号。
"""
if __name__=='__main__':
    n,k = list(map(int,input().split()))
    num = list(map(int,input().split()))
    res = []
    for i in range(n):
        l = max(0,i-num[i])
        r = min(n,i+num[i]+1)
        res.append((l,r))
    dp = [0 for _ in range(n+1)]
    for i in range(n):
        dp[res[i][0]] += 1
        dp[res[i][1]] -= 1
    count = 0
    temp = 0
    for i in range(len(dp)):
        temp += dp[i]
        if temp >= k:
            count += 1
    print(count)