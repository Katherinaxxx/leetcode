#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/10/9 下午9:27
@Author : Catherinexxx
@Site : 
@File : 154 LCOF11 旋转数组的最小数字.py
@Software: PyCharm
"""
"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 比较第一个元素和 乱序的第一个元素即可 O(n)time O(1)space
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if len(numbers) == 1: return numbers[0]
        i = 0
        while i+1 < len(numbers):
            if numbers[i+1] < numbers[i]:
                return min(numbers[0], numbers[i+1])
            else:
                i += 1
        return numbers[0]
