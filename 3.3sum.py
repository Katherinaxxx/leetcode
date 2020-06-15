#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/17 上午11:02
@Author : Catherinexxx
@Site : 
@File : 3.3sum.py
@Software: PyCharm
"""

# // a + b = -c (target)
# // 1、暴力 三重循环 O(n^3) O(1)
# // 2.hashmap来记录 O(n^2) O(n)
# // 3、双指针往中间推移 （trick） O(n^2) O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # 双指针关键
        for i in range(len(nums)-2):
            # 跳过重复的
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, h = i+1, len(nums)-1
            while l < h:
                s = nums[i] + nums[l] + nums[h]
                if s < 0:
                    l += 1
                elif s > 0:
                    h -= 1
                else:
                    res.append([nums[i], nums[l], nums[h]])
                    # 跳过一样的排除重复
                    while l < h and nums[l] == nums[l+1]:
                        l += 1
                    while l < h and nums[h] == nums[h-1]:
                        h -= 1
                    l += 1; h -= 1
        return res