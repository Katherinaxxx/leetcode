#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/24 下午11:38
@Author : Catherinexxx
@Site : 
@File : 292. Nim 游戏.py
@Software: PyCharm
"""
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4 != 0