#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/27 下午1:36
@Author : Catherinexxx
@Site : 
@File : 74. Subarray Sums Divisible by K.py
@Software: PyCharm
"""
"""
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
"""
# 前缀和 保存和 O(n^2)time 超时
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        d = {}
        acc = cnt = 0
        for x in A:
            acc += x
            if acc % K == 0:
                cnt += 1
            for y in d:
                if (acc-y) % K == 0:
                    cnt += d[y]
            if acc in d:
                d[acc] += 1
            else:
                d[acc] = 1
        return cnt

# 前缀和优化 O(n)time
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        pre_mod = 0  # 存储（当前位置的上一个位置的前缀和的余数加上当前位置的值）对K的余数
        presum_count = collections.defaultdict(int)
        presum_count[0] = 1
        for i in range(len(A)):
            pre_mod = (pre_mod + A[i]) % K
            # 下面这行感觉最不好理解
            res += presum_count[pre_mod]  # 如果能在dict中找到相同的pre_mod，说明当前节点前的某个位置的前缀和到当前位置的前缀和间存在若干个K
            presum_count[pre_mod] += 1
        return res