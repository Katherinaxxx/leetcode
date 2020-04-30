#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/28 下午3:07
@Author : Catherinexxx
@Site : 
@File : 448. Find All Numbers Disappeared in an Array.py
@Software: PyCharm
"""
'''
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 每个数对应位置abs(nums[i]) - 1 如果第一次出现就把对应位置上的数变为负数 最后为正数对应位置的就是未出现过的
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            loc = abs(nums[i]) - 1
            if nums[loc] > 0:
                nums[loc] = -nums[loc]
        for idx, val in enumerate(nums, 1):
            if val > 0:
                res.append(idx)
        return res