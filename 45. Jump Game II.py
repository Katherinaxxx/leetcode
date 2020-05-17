#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/4 下午9:59
@Author : Catherinexxx
@Site : 
@File : 45. Jump Game II.py
@Software: PyCharm
"""
'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 贪心 可从后往前 但是会超时 以下是前往后

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])       # i + nums[i]表示当前位置接下来能达到的最远下标
                if i == end:
                    end = maxPos
                    step += 1
        return step
