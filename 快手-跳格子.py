#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/3/22 下午6:26
@Author : Catherinexxx
@Site : 
@File : 快手-跳格子.py
@Software: PyCharm
"""
"""有位老铁设计了一个跳格子游戏，游戏有N个格子顺序排成一行，编号从1到N，每个格子有点数Qi，有标记Li（标记的范围是1-M），每次跳格子，要选择一个格子a，以任意正偶数距离x跳到格子b，如果格子b在游戏区域内，且La=Lb，则称为一次合法跳跃，获得的分数是(a + b) * (Qa + Qb)。
在继续设计游戏玩法时，这位老铁纠结了很久，于是他决定放弃……但是他想知道所有合法跳跃总共能获得多少分。
"""

# 超时
nm = list(map(int, input().split(' ')))
n, m = nm[0], nm[1]
s = list(map(int, input().split(' ')))
l = list(map(int, input().split(' ')))


def solution(n, s, l):
    if n <= 2:
        return 0
    if n == 3:
        return (1 + 3) * (s[0] + s[2])

    score = 0
    for i in range(n - 2):
        j = i
        while j + 2 <= n - 1:
            j += 2
            if l[i] == l[j]:
                score += (i + j + 2) * (s[i] + s[j])
            else:
                continue
    return score


res = solution(n, s, l)
print(res % 10007)