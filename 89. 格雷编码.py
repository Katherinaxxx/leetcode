#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/24 下午11:32
@Author : Catherinexxx
@Site : 
@File : 89. 格雷编码.py
@Software: PyCharm
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ i>>1 for i in range(1<<n)]