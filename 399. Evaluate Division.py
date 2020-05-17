#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/16 上午10:55
@Author : Catherinexxx
@Site : 
@File : 399. Evaluate Division.py
@Software: PyCharm
"""
"""
给出方程式 A / B = k, 其中 A 和 B 均为代表字符串的变量， k 是一个浮点型数字。
根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 构造图，equations的第一项除以第二项等于value里的对应值，第二项除以第一项等于其倒数
        graph = {}
        for (x, y), v in zip(equations, values):
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y: v}
            if y in graph:
                graph[y][x] = 1 / v
            else:
                graph[y] = {x: 1 / v}

        # dfs找寻从s到t的路径并返回结果叠乘后的边权重即结果
        def dfs(s, t) -> int:
            if s not in graph:
                return -1
            if t == s:
                return 1
            for node in graph[s].keys():
                if node == t:
                    return graph[s][node]
                elif node not in visited:
                    visited.add(node)  # 添加到已访问避免重复遍历
                    v = dfs(node, t)
                    if v != -1:
                        return graph[s][node] * v
            return -1

        # 逐个计算query的值
        res = []
        for qs, qt in queries:
            visited = set()
            res.append(dfs(qs, qt))
        return res
