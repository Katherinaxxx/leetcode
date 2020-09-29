#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/9/29 下午8:02
@Author : Catherinexxx
@Site : 
@File : 最少完全平方数.py
@Software: PyCharm
"""
"""
一个数最少能由几个完全平方数组成
"""
import math

def is_sqrt(n):
    sqrt=math.sqrt(n)
    return sqrt-int(sqrt)==0

def get_res(n):
    dp=[1]+[0]*n
    if(is_sqrt(n)):return 1
    for i in range(1,n+1):
        if(is_sqrt(i)):
            dp[i]=1
            continue
        dp[i]=dp[i-1]+1#i可能取到的最大数。最不济也能上一个数加一个1得到，所以是+1(dp[1])#然后循环取最小
        for j in range(i-1,(i+1)//2-1,-1):
            dp[i]=min(dp[i],dp[i-j]+dp[j])#是直接i组成平方数大，还是拆成2个数，分别平方数求和大。从大到小遍历更快。
            if(dp[i]==2):break#剪枝
    return dp[n]

print(get_res(13))#2