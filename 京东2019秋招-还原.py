#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/26 下午9:25
@Author : Catherinexxx
@Site : 
@File : 京东2019秋招-还原.py
@Software: PyCharm
"""

n = int(input())
nums = list(map(int, input().split()))

res = 0
for i,x in enumerate(nums):
    if x == 0:
        if i == 0:
            res +=