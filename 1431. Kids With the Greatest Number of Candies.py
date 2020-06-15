#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/1 上午11:41
@Author : Catherinexxx
@Site : 
@File : 1431. Kids With the Greatest Number of Candies.py
@Software: PyCharm
"""
"""
给你一个数组 candies 和一个整数 extraCandies ，其中 candies[i] 代表第 i 个孩子拥有的糖果数目。

对每一个孩子，检查是否存在一种方案，将额外的 extraCandies 个糖果分配给孩子们之后，此孩子有 最多 的糖果。注意，允许有多个孩子同时拥有 最多 的糖果数目。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# O(n)time O(n)space
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        p = max(candies)
        for x in candies:
            if x + extraCandies < p:
                res.append(False)
            else:
                res.append(True)
        return res