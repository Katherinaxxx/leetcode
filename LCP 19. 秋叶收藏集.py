#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/10/1 下午4:49
@Author : Catherinexxx
@Site : 
@File : LCP 19. 秋叶收藏集.py
@Software: PyCharm
"""
"""
小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/UlBDOe
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# dp time O(n) space O(3n)=O(n)
# dp[i][0] 截止目前全为r    dp[i][0] = dp[i-1][0] + (leaves[i]!='r')
# dp[i][1] 截止目前r+y        dp[i][1]
# dp[i][2] 截止目前r+y+r
# return dp[-1][2]
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        # 最终需要红黄红
        # 维持3种状态，分别为截止目前全部红色，在截止目前全红的基础上变为黄色，以及变为黄色的基础上全部红色
        n = len(leaves)
        dp = [[float('inf')]*3 for _ in range(n)]
        dp[0][0] = 0 if leaves[0] == 'r' else 1

        for i in range(n):
            dp[i][0] = min(dp[i][0],dp[i-1][0] + (leaves[i]!='r'))
            dp[i][1] = min(dp[i-1][1]+(leaves[i]!='y'),dp[i-1][0] +(leaves[i]!='y') )
            dp[i][2] = min(dp[i-1][2]+(leaves[i]!='r'),dp[i-1][1]+(leaves[i]!='r'))
        return dp[n-1][2]

