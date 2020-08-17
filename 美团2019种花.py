#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/15 下午2:35
@Author : Catherinexxx
@Site : 
@File : 美团2019种花.py
@Software: PyCharm
"""
"""
公园里有N个花园，初始时每个花园里都没有种花，园丁将花园从1到N编号并计划在编号为i的花园里恰好种A_i朵花，他每天会选择一个区间[L，R]（1≤L≤R≤N）并在编号为L到R的花园里各种一朵花，那么园丁至少要花多少天才能完成计划？
"""
n = int(input())
num = list(map(int, input().split()))
count = 0
for i in range(n - 1):
    count += max(num[i] - num[i + 1], 0)
print(count + num[-1])