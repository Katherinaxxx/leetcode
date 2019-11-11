#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/4 下午3:22
@Author : Catherinexxx
@Site : 
@File : 860. Lemonade Change.py
@Software: PyCharm
"""

# 贪心算法
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in bills:
            if i == 5:
                five += 1
                continue
            elif i == 10 and five:
                ten += 1
                five -= 1
            elif i == 20 and not ten and five >= 3:
                five -= 3
            elif i == 20 and ten and five:
                ten -= 1
                five -= 1
            else:
                return False
        return True