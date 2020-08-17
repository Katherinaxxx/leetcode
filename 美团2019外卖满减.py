#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/15 下午2:11
@Author : Catherinexxx
@Site : 
@File : 美团2019外卖满减.py
@Software: PyCharm
"""
# 直接
n, x = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
ans = {0 }
for c in a:
    for d in list(ans):
        ans.add(c + d)
ans = [c for c in ans if c >= x]
print(min(ans))