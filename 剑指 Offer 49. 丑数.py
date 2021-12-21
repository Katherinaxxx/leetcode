'''
Author: Catherine Xiong
Date: 2021-12-08 19:26:02
LastEditTime: 2021-12-08 19:26:03
LastEditors: Catherine Xiong
Description: 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
'''
"""DP 
设置3个索引a, b, c，分别记录前几个数已经被乘2， 乘3， 乘5了，比如a表示前(a-1)个数都已经乘过一次2了，下次应该乘2的是第a个数；b表示前(b-1)个数都已经乘过一次3了，下次应该乘3的是第b个数；c表示前(c-1)个数都已经乘过一次5了，下次应该乘5的是第c个数
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [0 for _ in range(n)], 0, 0, 0
        dp[0] = 1
        for i in range(1, n):
            a2, b3, c5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(a2, b3, c5)
            if dp[i] == a2: a += 1
            if dp[i] == b3: b += 1
            if dp[i] == c5: c += 1
        return dp[-1]
