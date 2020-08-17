#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/15 下午1:39
@Author : Catherinexxx
@Site : 
@File : 美团2019遍历图.py
@Software: PyCharm
"""
"""
给定一张包含N个点、N-1条边的无向连通图，节点从1到N编号，每条边的长度均为1。假设你从1号节点出发并打算遍历所有节点，那么总路程至少是多少？
"""

"""
n个点，n-1条边组成得图是无环图，所以要遍历所有点，最少得走法是所有边走俩两边再减去图中得最长路径，所以本题可以理解为，用bfs求图得最长路径
"""

from collections import defaultdict
d = defaultdict(list)
n = int(input())
for i in range(n-1):
    a,b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

visited = defaultdict(bool)
visited[1] = True
res = 0
stack = [1]
while len(stack) > 0:
    tmp = []
    while len(stack) > 0:
        t = stack.pop()
        for e in d[t]:
            if not visited[e]:
                visited[e] = True
                tmp.append(e)
    stack = tmp
    res += 1
print(2 * (n-1) - res + 1)