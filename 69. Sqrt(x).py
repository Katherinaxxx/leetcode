#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/30 下午2:37
@Author : Catherinexxx
@Site : 
@File : 69. Sqrt(x).py
@Software: PyCharm
"""

# # 二分法
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x == 0: return 0
#         left, right = 1, x//2   # 平方根一定不超过一半
#         while left < right:
#             mid = left + (right-left+1)//2
#             s = mid*mid
#             if  s > x:
#                 right = mid -1
#             else:
#                 left = mid
#         return left

# # 牛顿法
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r > x:
            r = (r + x/r) // 2
        return r