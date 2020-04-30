#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/2/18 下午1:07
@Author : Catherinexxx
@Site : 
@File : LCOF45.py
@Software: PyCharm
"""

# 两两组合比较
class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n=len(nums)
        if n==0:
            return ""
        for i in range(n):
            nums[i]=str(nums[i])
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]>nums[j]+nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
        return "".join(nums)