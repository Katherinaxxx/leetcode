#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/27 下午6:55
@Author : Catherinexxx
@Site : 
@File : 京东2020秋招.py
@Software: PyCharm
"""

# 滚球游戏 dp AC
# n = int(input())
# data = [list(map(int, input().strip().split())) for _ in range(n)]
#
# dp = [[0]*len(data[-1]) for _ in range(n)]
# dp[-1] = data[-1]
# for i in range(n-2, -1, -1):
#     div = (len(data[-1]) - len(data[i])) // 2
#     for j in range(len(data[i])):
#         dp[i][j+div] = max(dp[i+1][j-1+div], dp[i+1][j+div], dp[i+1][j+1+div]) + data[i][j]
# print(dp[0][(len(data[-1])-1)//2])


# # 数列变换 9
n = int(input())

def insert(num,i,x):

    return num[:i] + [x] + num[i:]

def delete(num,i):
    if i == len(num)-1:
        num.pop()
        return num
    else:
        return num[:i] + num[i+1:]

def show(num):
    num.pop(0)
    print(' '.join(num))
    return [0] + num

num = []
for _ in range(n):
    order = input().split()
    if order[0] == '1':
        num.insert(int(order[1])-1, order[2])
    elif order[0] == '2':
        num.pop(int(order[1])-1)
    else:
        print(' '.join(num))

# def insert(num,i,x):
#
#     return num[:i] + [x] + num[i:]
#
# def delete(num,i):
#     if i == len(num)-1:
#         num.pop()
#         return num
#     else:
#         return num[:i] + num[i+1:]
#
# def show(num):
#     num.pop(0)
#     print(' '.join(num))
#     return [0] + num
#
# num = [0]
# for _ in range(n):
#     order = input().split()
#     if order[0] == '1':
#         num = insert(num, int(order[1]), order[2])
#     elif order[0] == '2':
#         num = delete(num, int(order[1]))
#     else:
#         num = show(num)


