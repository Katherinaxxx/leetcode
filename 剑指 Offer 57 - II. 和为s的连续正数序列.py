#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/8/2 9:36 PM
@Author : Catherinexxx
@File : 剑指 Offer 57 - II. 和为s的连续正数序列.py
@Description: 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        a1, n = 1, target
        while n >= 2:
            a1 = target / n - (n-1) / 2
            if a1 > 0 and a1 % 1 == 0:
                res.append([int(a1)+i for i in range(n)])
            n -= 1
        return res
