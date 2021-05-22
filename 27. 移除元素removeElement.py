#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/4/19 7:24 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 27. 移除元素removeElement.py
@Description: 
"""
# 双指针 i从前往后 遇到val 则把ij交换 j-1 i继续 直到ij相等 返回j+1
# 时间复杂度O(n)  空间复杂度O(1)
class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j = len(nums) # 若len(nums)-1 则会对[1]一个元素出错
        while i<j:
            if nums[i]==val:
                nums[i],nums[j-1]=nums[j-1],nums[i]
                j-=1
            else:
                i+=1
        return j
