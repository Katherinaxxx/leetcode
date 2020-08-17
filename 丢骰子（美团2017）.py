#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/13 下午10:56
@Author : Catherinexxx
@Site : 
@File : 丢骰子（美团2017）.py
@Software: PyCharm
"""
"""
大富翁游戏，玩家根据骰子的点数决定走的步数，即骰子点数为1时可以走一步，点数为2时可以走两步，点数为n时可以走n步。求玩家走到第n步（n<=骰子最大点数且是方法的唯一入参）时，总共有多少种投骰子的方法。
"""
# 1
n = int(input())
def solution(n):
    dp = [0]
    for i in range(n):
        dp.append(sum(dp)+1)
    return dp[-1]
print(solution(n))

# 2 递推公式 an=a1+...+an-1=2^(n-1)
print(2**(n-1))