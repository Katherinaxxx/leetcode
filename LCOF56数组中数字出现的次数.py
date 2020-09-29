#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/9/24 下午7:22
@Author : Catherinexxx
@Site : 
@File : LCOF56数组中数字出现的次数.py
@Software: PyCharm
"""
"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
"""
class Solution(object):
    def singleNumbers(self, nums):
        ret, index = 0, 0
        for n in nums:
            ret ^= n
        # 找从右向左数第几位不同，也就是第index位
        # 这一步其实可以根据n & (-n)的快捷方式获得，不过对位运算掌握不是那么熟练的话，记结论容易忘，不如理解实质
        while ret & 1 == 0:
            index += 1
            ret >>= 1
        r1, r2 = 0, 0
        for n in nums:
            if (n >> index) & 1 == 0:
                r1 ^= n
            else:
                r2 ^= n
        return [r1, r2]