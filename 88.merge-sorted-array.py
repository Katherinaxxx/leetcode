#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/16 下午1:53
@Author : Catherinexxx
@Site : 
@File : 88.merge-sorted-array.py
@Software: PyCharm
"""


class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = 0, 0
        new = []
        while i <m :
            while j <n and nums1[i]>=nums2[j]:
                new.append(nums2[j])
                j = j+1
            new.append(nums1[i])
            i = i+1
        if i==m:
            while j<n:
                new.append(nums2[j])
                j = j + 1
        nums1 = new
        print(nums1)
#
# class Solution:
#     def merge(self, nums1, m, nums2, n) -> None:
#         sort = []
#         i, j = 0, 0
#         while len(sort) < m+n:
#             if sort == []:
#                 if nums1[0] <= nums2[0]:
#                     sort.append(nums1[0])
#                     i = 1
#                 else:
#                     sort.append(nums2[0])
#                     j = 1
#             top = sort[-1]
#             while nums1[i] > top and nums1[i] < nums2[j]:
#                 sort.append(nums1[i])
#                 top = sort[-1]
#                 i += 1
#             while nums2[j] > top and nums1[i] > nums2[j]:
#                 sort.append(nums2[j])
#                 top = sort[-1]
#                 j += 1
#         nums1 = sort
#         print(nums1)


Solution().merge([1,12],2,[2,5,6],3)
