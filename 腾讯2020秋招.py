#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/23 下午8:03
@Author : Catherinexxx
@Site : 
@File : 腾讯2020秋招.py
@Software: PyCharm
"""
# 1 有效括号
# s = input()
def solution(s):
    dic = {")": "(", "]": "["}  # 右 -> 左
    stack = []  # 存左括号
    tmp = 0
    for char in s:
        if char in dic: # you
            tmp_s = []
            while stack:
                top = stack.pop()
                if dic[char] == top:
                    tmp += 1
                    continue
                tmp_s.append(top)
            # hui
            for x in tmp_s:
                stack.append(x)
        else:
            stack.append(char)


    return len(s)-tmp*2

print(solution(')([]]([(](])))([]()()]([][[)[()[)]([[(])][][[[([)]'))   # 4


# print(solution(')(][][)('))
#
# 2 面积（积分）输出格式坑了
# n = int(input())
# for _ in range(n):
#     a, b,c,d = list(map(int,input().split()))
#     res = a/3*(d**3-c**3)+0.5*(d**2-c**2)+b*(d-c)
#     ans = abs(res)
# print("%.6f"%ans)


# 3 选队长 
# n = int(input())
# import math
# def helper(n):
#     res = 1
#     for x in range(1, n + 1):
#         res *= x
#     return res
# res = 0
# for i in range(1, n + 1):
#     # res += i * (helper(n) / (helper(i) * helper(n - i)))
#     res += i * (math.factorial(n) / (math.factorial(i) * math.factorial(n - i)))
# print(int(res % (10 ** 9 + 7)))
n = int(input())

mod = 10 ** 9 + 7


def cal(x, n, p):
    res = 1
    while n > 0:
        if n % 2:
            res = res * x % p
        x = x * x % p
        n = n//2
    return res


ans = n * cal(2, n - 1, mod)
ans = ans % mod
print(ans)

# 5 寻宝问题 双向路径 单向传送门
from collections import defaultdict
A = defaultdict(list)
B = defaultdict(list)
n,m,k = list(map(int,input().split()))
# 双向路径
for _ in range(m):
    x,y,_ = list(map(int,input().split()))
    A[x].append(y)
    A[y].append(x)
# 单向门 走他不算消耗
for _ in range(k):
    x, y = list(map(int, input().split()))
    B[x].append(y)
ans = float('inf')
dp = [ans]*(n+1)
dp[1] = 0
for i in range(100):
    # 单向门不增加消耗
    for k,v in B.items():
        for j in v:
            dp[j] = min(dp[j], dp[k])
    # 双向路径增加消耗
    for k, v in A.items():
        for j in v:
            dp[j] = min(dp[j], dp[k] + 1)
print(dp[n])



############
# 1
def length(nums):
    size = len(nums)
    if size <= 1:
        return size

    dp = [1] * size
    for i in range(1, size):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
def solution(s,n):
    res = 0
    for i in range(1,n):
        if s[i] in s[i+1:]:
            j = s[i+1:].index(s[i]) + i + 1
            left = length(s[:i][::-1])
            right = length(s[j+1:])
            res = max(res, 2*(min(left, right)+1))
    return res
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    print(solution(s,n))



# 2
l, d = list(map(int, input().split()))

# 4 60
def helper(nums1, nums2):
    return sorted(nums1)==sorted(nums2)
    # tmp = [x-y for x in nums1 for y in nums2]
    # return sum(tmp)==0
def main(data, n):
    for i in range(n-1):
        for j in range(i,n):
            if helper(data[i], data[j]):
                return True
    return False
N = int(input())
for _ in range(N):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    if main(data, n):
        print("YES")
    else:
        print("NO")