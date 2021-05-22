#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/4/21 8:00 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 剑指 Offer 17. 打印从1到最大的n位数.py
@Description: 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
"""
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [x for x in range(1, 10**n)]