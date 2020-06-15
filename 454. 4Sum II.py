#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/29 下午6:25
@Author : Catherinexxx
@Site : 
@File : 454. 4Sum II.py
@Software: PyCharm
"""
"""
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# hash 前两个求和 后两个求和 在前面找 O(n^2)time O(n)space
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        lookup = collections.defaultdict(int)
        res = 0
        for a in A:
            for b in B:
                lookup[a+b] += 1
        for c in C:
            for d in D:
                res += lookup[-(c + d)]
        return res
