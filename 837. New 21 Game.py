#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/3 下午12:56
@Author : Catherinexxx
@Site : 
@File : 837. New 21 Game.py
@Software: PyCharm
"""
"""
爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：

爱丽丝以 0 分开始，并在她的得分少于 K 分时抽取数字。 抽取时，她从 [1, W] 的范围中随机获得一个整数作为分数进行累计，其中 W 是整数。 每次抽取都是独立的，其结果具有相同的概率。

当爱丽丝获得不少于 K 分时，她就停止抽取数字。 爱丽丝的分数不超过 N 的概率是多少？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/new-21-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# DP 填格子 太秀了 O(n)tiime O(n)space
# 假设dp[x]为她手上牌面为x时，能获胜的概率，那么这个概率应该是：
# dp[x]=1/w * (dp[x+1]+dp[x+2]+dp[x+3]...+dp[x+w])
# 因为抽取的牌面机会都是均等的，她能抽取的面值在[1,W]之间，所以将概率之和平均一下就是dp[x]的概率。
# x最多能到K-1，因为当大于等于K时，爱丽丝会停止抽牌，所以当游戏结束时，即爱丽丝停止抽牌时，她可能达到的最大牌面是K+W-1，而一开始她的牌面是0，所以我们用一个长度为K+W的dp数组来保存她在所有面值下的胜率。
# 最后dp[0]，也就是最开始爱丽丝还没有抽牌，她的牌面为0时的胜率，这个就是我们的答案。

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp=[None]*(K+W)
        s=0
        for i in range(K,K+W):          # 填蓝色的格子
            dp[i] = 1 if i<=N else 0
            s+=dp[i]
        for i in range(K-1,-1,-1):      # 填橘黄色格子
            dp[i]=s/W
            s=s-dp[i+W]+dp[i]
        return dp[0]
