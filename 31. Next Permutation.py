#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/21 下午1:31
@Author : Catherinexxx
@Site : 
@File : 31. Next Permutation.py
@Software: PyCharm
"""
"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 从倒数第二往前遍历 找到他后面最小的比他大的数 交换位置 后面升序
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                subNums = sorted(nums[i:len(nums)])
                for j in subNums:
                    if j>nums[i-1]:
                        newSub=j
                        break
                k = nums.index(newSub,i)
                nums[i-1],nums[k] = nums[k],nums[i-1]
                nums[i:] = sorted(nums[i:])
                return nums
        return nums.sort()