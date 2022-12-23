"""
Date: 2022-12-15 10:39:32
LastEditors: yhxiong
LastEditTime: 2022-12-22 16:18:19
Description: 
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/25 下午2:42
@Author : Catherinexxx
@Site : 
@File : 169.majority-element.py
@Software: PyCharm
"""
# # 1、暴力 遍历找多的
# # 2、hash表 找多的
# class Solution:
#     def majorityElement(self, nums):
#         counts = collections.Counter(nums)      # 没用过，学习了
#         return max(counts.keys(), key=counts.get)


# 2、数学推理
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[len(nums)//2]
        
    def majorityElement(self, nums):
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate