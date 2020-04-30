#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/3/22 下午6:22
@Author : Catherinexxx
@Site : 
@File : 快手-运动会.py
@Software: PyCharm
"""
"""
一年一度的快手运动会又要开始了，同学们终于有一天可以离开鼠标键盘显示器，全身心的投入到各种体育项目中。UED设计师小红虽然没有参加体育项目，但她的责任重大，因为她是拉拉队的队长，她需要在每个项目中为参赛的同学们加油助威。
因为运动会的项目众多，很多项目在同一时间会同时进行着。作为拉拉队长，小红需要遵守以下规则：
不能同时给多个体育项目加油助威
给每个体育项目加油的时长必须超过项目时长的一半，每个体育项目只能加油一次
体育项目的开始和结束时间都是整点，如果项目进行到一半想要离开，也只能选择整点离开
不考虑往返于各个体育项目比赛场地中花费的时间
请帮小红设计一个算法，在已知所有体育项目日程的前提下，计算是否能在每个体育项目中为参赛的同学们加油。

说明
如果体育项目时长为2，超过时长的一半为2;
如果体育项目时长为3，超过时长的一半为2;
如果体育项目时长为4，超过时长的一半为3；
"""

# 我的 递归 80%通过
num = int(input())
time = []
for i in range(num):
    time.append(list(map(int, input().split(' '))))

res = []

def recursion(state, now):
    if state == [1] * num:
        res.append(1)
        return
    for i in range(num):
        if state[i] == 1:
            continue
        else:
            if now == 0:
                now = time[i][0]
            spend = (time[i][1] - time[i][0] + 1) // 2
            if time[i][0] <= now <= time[i][1] + spend:
                now += spend
                state[i] == 1
                recursion(state, now)
            else:
                break


state = [0] * num
recursion(state, 0)

print(1) if 1 in res else print(-1)