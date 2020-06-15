#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/2 上午11:20
@Author : Catherinexxx
@Site : 
@File : 面试题64. 求1+2+…+n LCOF.py
@Software: PyCharm
"""
"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""

# math (1+n)n/2 O(1)time
class Solution:
    def sumNums(self, n: int) -> int:
        return (1+n)*n//2