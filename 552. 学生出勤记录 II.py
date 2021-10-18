#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/8/19 12:27 AM
@Author : Catherinexxx
@File : 552. 学生出勤记录 II.py
@Description: 
"""
# 超出最深
class Solution:
    def checkRecord(self, n: int) -> int:
        self.res = 0
        def dfs(length, q, l):
            if length == n:
                self.res += 1
                return
            if q == 0:
                dfs(n+1, q+1, 0)
            if l < 2:
                dfs(n+1, q, l+1)
            dfs(n+1, q, 0)
        dfs(0, 0, 0)
        return self.res

# 状态
class Solution:
    def checkRecord(self, n: int) -> int:
        # 这道题，整一个状态机即可
        # 考虑A的数量，与字符串结尾处L的数量，一共6种状态
        #(A=0,结尾处连续L=0),(0,1),(0,2),(1,0),(1,1),(1,2)
        a,b,c,d,e,f = 1,0,0,0,0,0
        for i in range(n):
            a,b,c,d,e,f = a+b+c,a,b,a+b+c+d+e+f,d,e
            a %= (10**9+7)
            b %= (10**9+7)
            c %= (10**9+7)
            d %= (10**9+7)
            e %= (10**9+7)
            f %= (10**9+7)
            #print(i,a,b,c,d,e,f)
        return (a+b+c+d+e+f)%(10**9+7)
