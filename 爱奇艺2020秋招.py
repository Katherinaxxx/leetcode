#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/23 下午2:58
@Author : Catherinexxx
@Site : 
@File : 爱奇艺2020秋招.py
@Software: PyCharm
"""
# 分词结果修改
ori = input().split(' ')
target = input().split(' ')
i, j, l = 0, 0, 0

for x in ori:
    l += len(x)
res = []
while i < l and j < len(target):
    if ori[i] not in target[j] and target[j] not in ori[i]:
        res.append(ori[i])
        i += 1
    elif ori[i] in target[j] and target[j] in ori[i]:   # quanbao
        tmp_i = ori[i].index(target[j])
        if tmp_i != 0:
            res.append(ori[:tmp_i])
            i += tmp_i
        res.append(target[j])
        i += len(target[j])
        j += 1
    elif ori[i] in target[j] and target[j] not in ori[i]:   # a cab
        tmp_s = ''
        while tmp_s != target[j]:
            tmp_j = target[j].index(ori[i])
            if tmp_j != 0:
                res.append(target[:tmp_j])
                i += tmp_j
            tmp_s +=
            i += len(target[j])



