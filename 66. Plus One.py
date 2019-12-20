#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/12/13 下午3:16
@Author : Catherinexxx
@Site : 
@File : 66. Plus One.py
@Software: PyCharm
"""
# 别人的解法也没看有多巧妙
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [0] + digits
        for i in range(len(digits)-1, -1, -1):
            if 0 <= digits[i] <= 8:
                digits[i] += 1
                return digits if digits[0]!=0 else digits[1:]
            else:
                digits[i] = 0