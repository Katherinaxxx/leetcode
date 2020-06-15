#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/3 下午1:24
@Author : Catherinexxx
@Site : 
@File : 7. Reverse Integer.py
@Software: PyCharm
"""
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""


# 暴力
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            f = 1
            sx = str(x)
        else:
            f = -1
            sx = str(abs(x))

        l = len(sx) if sx[-1] != '0' else len(sx) - 1
        res = 0
        for i in range(l):
            res += int(sx[i]) * 10 ** i
        return f * res if -2147483648 < f * res < 2147483647 else 0


class Solution:
    def reverse(
            self,
            x: int) -> int:

        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > boundry:
                return 0
            y //= 10
        return res if x > 0 else -res


class Solution(object):
    def reverse(self, x):
        ans = 0
        flag = 1
        if x < 0:
            x = -x;
            flag = -flag

        while x != 0:
            cur = x % 10
            ans = ans * 10 + cur
            x //= 10
        return ans * flag if -2 ** 31 < ans * flag < 2 ** 31 else 0