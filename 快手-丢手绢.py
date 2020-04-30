#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/3/22 下午6:32
@Author : Catherinexxx
@Site : 
@File : 快手-丢手绢.py
@Software: PyCharm
"""

"""有n 个老铁（编号为 1 到n）正在玩丢手绢。在游戏里每人会把当前手里的手绢丢给一个固定的人，编号为Ti。 游戏开始时，每人手里有自己的手绢。之后每一轮中，所有人会同时将自己当前手里的手绢全部丢给接收的对象。当有人重新拿到自己的手绢时，游戏结束。
那么游戏几轮会结束呢？
"""

"""思想：
基于判环算法，去掉所有不构成环的顶点和边
对于剩下的节点，统计有多少个环&环中顶点个数
"""
# https://www.nowcoder.com/test/question/done?tid=31710225&qid=907554#summary

def f():
    n = int(input())

    to = [int(item) - 1 for item in input().split()]
    in_degree = [0] * n
    for i in range(n):
        in_degree[to[i]] += 1
    stack = []
    for i in range(n):
        if in_degree[i] == 0:
            stack.append(i)
    while len(stack) != 0:
        top = stack[-1]
        in_degree[top] -= 1  # in_degree==-1,则代表删除了
        stack.pop(-1)
        in_degree[to[top]] -= 1
        if in_degree[to[top]] == 0:
            stack.append(to[top])
    min_num = 200000
    for i in range(n):
        if in_degree[i] == -1:
            continue
        else:
            start = i
            num = 1
            while to[i] != start:
                i = to[i]
                num += 1
                in_degree[i] = -1  # 同一个圈内的就不重复计算环了
            min_num = min(min_num, num)
    return min_num


ans = f()
print(ans)