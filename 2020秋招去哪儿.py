#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/9/23 下午7:09
@Author : Catherinexxx
@Site : 
@File : 2020秋招去哪儿.py
@Software: PyCharm
"""
# 1 Cmn ac
# m = int(input())
# n = int(input())
def helper(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
def mul(start, end):
    res = 1
    for i in range(start, end-1, -1):
        res *= i
    return res

def main1(m,n):
    return helper(m)//(helper(m-n)*helper(n))
def main2(m, n):
    return mul(m, m-n+1)/ mul(n, 1)
# print(main2(4, 2))
print(main1(4,2))

# 2 最长单调递增子串 45
# n = int(input())
# nums1 = ''.join(input().split())
# nums2 = ''.join(input().split())
n=7
nums1 = ''.join('a b c d e f g'.split())
nums2 = ''.join('b d a c f g e'.split())
d = {}
for i, x in enumerate(nums1):
    d[x] = str(i)
nums = ''
for x in nums2:
    nums += d[x]

def main(nums):
    size = len(nums)
    if size <= 1:
        return size

    dp = [1] * size
    for i in range(1, size):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def main(nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size
# print(main(nums))

# 3 德州扑克 ac
n = int(input())
inputData = input().split()
# n=5
# inputData = 'SA SK SQ SJ S10'.split()
d = {'J':11,'Q':12, 'K':13, 'A':14, '2':2, '3':3, '4':4, '5':5, '6':6, \
     '7':7, '8':8, '9':9, '10':10}

data = [(x[0], d[x[1:]]) for x in inputData]
data = sorted(data, key=lambda x: x[1])

hua = [x[0] for x in data]
dian = [x[1] for x in data]

def helper(l):
    if 2 in l and 14 in l:
        l = [1] + l[:-1]
    for i in range(1, len(l)):
        if l[i] - l[i-1] != 1:
            return False
    return True
def main(hua, dian, n):
    res = 'GaoPai'
    if n == 2 and dian[0] == dian[1]:
        res = 'YiDui'
    if n == 4 and dian[0] == dian[1] and dian[2] == dian[3]:
        res = 'LiangDui'
    elif n == 5 and len(set(dian)) == 3:
        res = 'SanTiao'
    if len(set(hua)) == 1:
        res = 'TongHua'
        if helper(dian):
            res = 'TongHuaShun'
            if 14 in dian:
                res = 'HuangJiaTongHuaShun'
    elif helper(dian):
        res = 'ShunZi'
    if n == 5 and len(set(dian)) == 2:
        res = 'HuLu'
    return res

# print(main(hua, dian, n))
