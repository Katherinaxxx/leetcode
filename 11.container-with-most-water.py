#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/17 上午10:54
@Author : Catherinexxx
@Site : 
@File : 11.container-with-most-water.py
@Software: PyCharm
"""
# 1.暴力枚举遍历 O(n^2)
# 2. O(n) 左右边界中间收敛：左右夹逼

class Solution:
    def maxArea(self, a: List[int]) -> int:
        i, j, max_area = 0, len(a) - 1, 0
        while i < j:
            if a[i] < a[j]:
                max_area = max(max_area, (j-i)*a[i])
                i += 1
            else:
                max_area = max(max_area, (j-i)*a[j])
                j -= 1
        return max_area


# # java
# //2. O(n) 左右边界中间收敛：左右夹逼
#
# class Solution {
#     public int maxArea(int[] a) {
#         int max = 0;
#         for (int i=0, j=a.length-1; i<j;) {
#             int minheight = a[i] < a[j] ? a[i++]:a[j--];
#             int area = (j-i+1)*minheight;
#             max = Math.max(max, area);
#         }
#         return max;
#     }
# }