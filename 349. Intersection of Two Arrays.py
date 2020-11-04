#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/11/2 下午11:16
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 349. Intersection of Two Arrays 两个数组的交集
@Description: 
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if not nums1 or not nums2: return res
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums1 = set(nums1)
        res = [x for x in nums1 if x in nums2]
        return res