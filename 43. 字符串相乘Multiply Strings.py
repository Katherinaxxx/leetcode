#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/24 下午11:27
@Author : Catherinexxx
@Site : 
@File : 43. 字符串相乘Multiply Strings.py
@Software: PyCharm
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 将字符串反转
        a = num1[::-1]
        b = num2[::-1]
        res = 0
        # 先循环num2
        # 假如num1 = 123 num2 = 456
        # 则从6 * 3 * 0 + 6 * 2 * 10 + 6 * 1 * 100开始
        for i, x in enumerate(b):
            temp_res = 0
            for j, y in enumerate(a):
                # 将6*123的结果加到临时变量中
                temp_res += int(x) * int(y) * 10 ** j
            # 根据位数添加0 便于之后的相加
            res += temp_res * 10 ** i

        return str(res)