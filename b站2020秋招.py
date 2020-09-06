#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/9/4 下午7:34
@Author : Catherinexxx
@Site : 
@File : b站2020秋招.py
@Software: PyCharm
"""
# 最长回文子串 dp
s = input()


size = len(s)
dp = [[False for _ in range(size)] for _ in range(size)]

longest_l = 1
res = s[0]

for r in range(1, size):
    for l in range(r):
        if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
            dp[l][r] = True
            cur_len = r - l + 1
            if cur_len > longest_l:
                longest_l = cur_len
                res = s[l:r + 1]
print(res)

# 最大子序列和 dp 负数则更新res
nums = list(map(int, input().split(',')))
res = nums[0]
for i in range(1,len(nums)):
    nums[i] = max(nums[i], nums[i-1] + nums[i])
    res = max(res, nums[i])
print(res)

# 大鱼吃小鱼 看有几段递减子串
n = int(input())
nums = list(map(int, input().split()))
res = 0

def solution(nums):
    if nums == sorted(nums):
        print(0)
        return
    while True:
        s = []
        for i in range(len(nums)-1-1, -1, -1):
            if nums[i] < nums[i+1]:
                s.append(nums[i])

        if len(s)<len(nums):
            res += 1
            nums = s[::-1]
        else:
            print(res)
            return
solution(nums)




