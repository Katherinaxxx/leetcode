#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/15 下午1:38
@Author : Catherinexxx
@Site : 
@File : 258. Add Digits.py
@Software: PyCharm
"""
"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
"""
# O(n)
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            nxt = 0
            while num > 0:
                nxt += num%10
                num //= 10
            num = nxt
        return num

# O(1)
class Solution:
    def addDigits(self, num: int) -> int:
        return num % 9 or 9 * bool(num)