#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/11/9 8:44 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 973. 最接近原点的 K 个点.py
@Description: 
"""
"""
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。
"""
# 遍历 O(n)time O(n)space
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # distance = [[x, x[0]**2+x[1]**2] for x in points]
        # sorted_distance = sorted(distance, key=lambda x: x[1])
        # return [x[0] for x in sorted_distance[:K]]
        return sorted(points, key=lambda x: x[0] * x[0] + x[1] * x[1])[:K]
# 堆排序
from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        queue = []
        distance = lambda x: points[x][0]**2 + points[x][1]**2
        length = len(points)
        for i in range(length):
            heappush(queue, (distance(i), points[i]))
        res = []
        for i in range(K):
            res.append(heappop(queue)[1])
        return res
