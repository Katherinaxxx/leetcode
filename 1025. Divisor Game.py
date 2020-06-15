#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/24 下午4:51
@Author : Catherinexxx
@Site : 
@File : 1025. Divisor Game.py
@Software: PyCharm
"""

"""
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divisor-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 归纳 奇数的约数一定是奇数或者1 因此下个数是偶数数
# 偶数的约数可以是1或奇数或偶数 因此下个数直接取-1 即偶数
# 因此 奇偶是交替的 如果偶数起手 则最后拿到2 赢 否则输
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

# # 最后当N==1时结束 换句话说N==2时的人赢
# class Solution:
#     def divisorGame(self, N: int) -> bool:
#         target = [0 for i in range(N+1)]
#         target[1] = 0 #若爱丽丝抽到1，则爱丽丝输
#         if N<=1:
#             return False
#         else:

#             target[2] = 1 #若爱丽丝抽到2，则爱丽丝赢
#             for i in range(3,N+1):
#                 for j in range(1,i//2):
#                     # 若j是i的余数且target[i-j]为假（0）的话，则代表当前为真（1）
#                     if i%j==0 and target[i-j]==0:
#                         target[i] = 1
#                         break
#             return target[N]==1