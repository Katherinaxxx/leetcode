#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/3/23 下午6:38
@Author : Catherinexxx
@Site : 
@File : 牛牛找工作.py
@Software: PyCharm
"""

"""为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在难度不超过自身能力值的情况下，牛牛选择报酬最高的工作。
在牛牛选定了自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，牛牛依然使用自己的标准来帮助小伙伴们。
牛牛的小伙伴太多了，于是他只好把这个任务交给了你。
"""

import sys
def main():
    lines = sys.stdin.readlines()
    lines = [line.strip().split() for line in lines if line.strip()]
    n, m = int(lines[0][0]), int(lines[0][1])   # 人数 工作数
    ai = [int(ai) for ai in lines[-1]]      # 各人能力
    allai = [0] * (n + m)   # 前m个为各职位要求
    salary = dict()
    for index, line in enumerate(lines[1:-1]):
        d, s = int(line[0]), int(line[1])   # 每个职位要求与报酬
        allai[index] = d
        salary[d] = s
    for index, a in enumerate(ai):
        allai[index + n] = a
        if a not in salary:
            salary[a] = 0
    maxSalary = 0
    allai.sort()
    for index in range(m + n):
        if maxSalary >  salary[allai[index]]:
            salary[allai[index]] = maxSalary
        else:
            maxSalary = salary[allai[index]]
    for index in range(m):
        print(salary[ai[index]])
if __name__ == '__main__':
    main()