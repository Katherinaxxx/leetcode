#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/3/22 下午1:23
@Author : Catherinexxx
@Site : 
@File : equation solution.py
@Software: PyCharm
"""

# 输入一元一次方程 求解 （牛客答案）
import sys


def solve(s):
    if not s:
        return -1
    a = s.split('=')
    alll = a[0] + '-' + a[1]
    L = []
    item = []
    for i in range(len(alll)):
        if alll[i] == '+':
            L.append('+' + str(i))
        if alll[i] == '-':
            L.append('-' + str(i))
            # print(L)
    L.append('+' + str(len(alll)))
    # print(L[-1][-1])
    if s[0] != '-':
        if s[0] == 'X':
            item.append('+1*' + alll[:int(L[0][-1])])
        else:
            item.append('+' + alll[:int(L[0][-1])])
    for i in range(1, len(L)):
        item.append(L[i - 1][0] + alll[int(L[i - 1][1:]) + 1:int(L[i][1:])])
    a = 0
    b = 0
    for i in item:
        if 'X' in i:
            a += int(i[:-2])
        else:
            b += int(i)
    if a == 0:
        res = -1  # 等于任何数都可以
    else:
        res = -b // a
    return res


s = sys.stdin.readline().strip()
res = solve(s)
print(res)