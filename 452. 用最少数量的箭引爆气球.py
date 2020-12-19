#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/11/23 10:03 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 452. 用最少数量的箭引爆气球.py
@Description: 在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。

一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 按右边界升序排序 初始右边界=第一个的右边界 然后比较每个的左边界 如果大于当前右边界 则更新右边界并且数目增加一
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if points == []: return 0
        res = 1
        # 按右边界排序
        points = sorted(points, key=lambda x:x[1])
        # 初始右边界
        right = points[0][1]
        for p in points[1:]:
            if p[0] > right:
                right = p[1]
                res += 1
        return res 

