#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/25 下午8:55
@Author : Catherinexxx
@Site : 
@File : 排序.py
@Software: PyCharm
"""
# shell
def shell(l):
    gap = len(l)
    while gap > 1:
        for i in range(gap, len(l)):
            for j in range(i%gap, i, gap):
                if l[i] < l[j]:
                    l[i], l[j] = l[j], l[i]
    return l
