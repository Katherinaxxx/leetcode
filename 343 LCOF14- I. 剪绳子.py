#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/11/12 8:55 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 343 LCOF14- I. 剪绳子 14- II. 剪绳子 II.py
@Description: 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# dp O(n*n!)  O(n)
# dp[i] 长度为i的绳子可以得到的最大乘积
# dp[i] = max(dp[i], max(j,dp[j])*max(i-j,dp[i-j]))
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i//2+1):
                dp[i] = max(dp[i],max(j,dp[j])*max(i-j,dp[i-j]))
        return dp[-1]

# 数学推导 O(1) 最优段长3
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n-1
        m = n % 3
        z = n // 3
        if m == 0: return 3**z
        elif m == 1: return 3**(z-1)*4
        else: return 3**z*2

# 2与1的区别在于需要每次计算都取余 只最后一次取余的话结果是不对的
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b, p, x, rem = n // 3 - 1, n % 3, 1000000007, 3 , 1
        while a > 0:
            if a % 2: rem = (rem * x) % p
            x = x ** 2 % p
            a //= 2
        if b == 0: return (rem * 3) % p # = 3^(a+1) % p
        if b == 1: return (rem * 4) % p # = 3^a * 4 % p
        return (rem * 6) % p # = 3^(a+1) * 2  % p
