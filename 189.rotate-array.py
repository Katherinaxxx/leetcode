#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/16 下午1:53
@Author : Catherinexxx
@Site : 
@File : 189.rotate-array.py
@Software: PyCharm
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        if k > len(nums): k = k % len(nums)
        temp = nums[-k:] + nums[:-k]

        for i in range(len(nums)):
            nums[i] = temp[i]