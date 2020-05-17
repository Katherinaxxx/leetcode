#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/6 下午3:31
@Author : Catherinexxx
@Site : 
@File : 238. Product of Array Except Selfv.py
@Software: PyCharm
"""
'''
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/product-of-array-except-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 左边乘积 右边乘积
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, k = [1] * len(nums), 1
        # 左边乘积
        for i in range(len(nums)):
            res[i] = k
            k *= nums[i]
        # 右边乘积
        k = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= k
            k *= nums[i]
        return res
