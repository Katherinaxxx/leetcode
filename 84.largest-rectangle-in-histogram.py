#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/18 下午1:51
@Author : Catherinexxx
@Site : 
@File : 84.largest-rectangle-in-histogram.py
@Software: PyCharm
"""

"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
"""
# 1、暴力求解 O(n^3)
# m = 0
# for i in 0,n-2:
#     for j in i+1, n-1:
#         area = (j-i+1)*minheight
#         m = max(m, area)

# 2、暴力2 O(n^2) 超时 枚举棒子 确定左右边界(左右第一个小于棒子的)
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         res = 0
#         n = len(heights)
#         for i in range(n):
#             left_i = i
#             right_i = i
#             while left_i >= 0 and heights[left_i] >= heights[i]:
#                 left_i -= 1
#             while right_i < n and heights[right_i] >= heights[i]:
#                 right_i += 1
#             res = max(res, (right_i - left_i - 1) * heights[i])
#         return res


# 2、栈 枚举棒子 确定左右边界 左边界知道的
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        # 边界要考虑
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            # print(stack)
            # 当下一个柱子小于栈顶元素 找到包括下一个柱子在内最矮的
            while stack and heights[stack[-1]] > heights[i]:
                cur = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[cur])
            stack.append(i)
        return res
