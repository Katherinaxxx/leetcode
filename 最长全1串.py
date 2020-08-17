#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/15 下午1:58
@Author : Catherinexxx
@Site : 
@File : 最长全1串.py
@Software: PyCharm
"""
"""
给你一个01字符串，定义答案=该串中最长的连续1的长度，现在你有至多K次机会，每次机会可以将串中的某个0改成1，现在问最大的可能答案
"""
n,k = list(map(int,input().split()))
num = list(map(int,input().split()))
i,j =0,0
res = 0
while j<n:
    if num[j]==1:
        j += 1
    elif k > 0:
        k -= 1
        j += 1
    else:
        res = max(res,j-i)
        while i<j and num[i]==1:
            i += 1
        j += 1
        i += 1
res = max(res,j-i)
print(res)