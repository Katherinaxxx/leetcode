#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/3/22 下午1:38
@Author : Catherinexxx
@Site : 
@File : 无重复字符最长子串.py
@Software: PyCharm
"""
s = input()
dict = {}
maxlength = 0
for i in s:
    if i not in dict:
        dict[i]=1
    else:
        maxlength = max(maxlength,len(dict))
        dict = {}
        dict[i] = 1
    #防止最长串在最后的情况，最后要再比较一次
    maxlength = max(maxlength,len(dict))
print(maxlength)