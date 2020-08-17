#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/16 下午1:49
@Author : Catherinexxx
@Site : 
@File : two-sum.py
@Software: PyCharm
"""
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

"""

# # 1.暴力遍历 O(n^2)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         res = [0, 0]
#         for i, a in enumerate(nums):
#             tmp = target - a
#             for j in range(i+1, len(nums)):
#                 if nums[j] == tmp:
#                     res = [i, j]
#                     return res

# 2. hashmap O(n)time O(n)space
# 别人的代码更简洁
class Solution:
    """
    采用Hash表的方法处理;
    通过构建一个新的字典表,将原本数组中的下标与值分别作为字典的value和Key
    再判断target与循环值的差值是否存在于字典中,从而得出结果
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            if target - n in dict:
                return [dict[target - n], i]
            dict[n] = i     # 不在hashmap中则添加新的

# # java
# class Solution {
#     public int[] twoSum(int[] nums, int target) {
#         int[] ints = new int[2];
#         a:
#         for (int i = 0; i < nums.length; i++) {
#             for (int j = 1; j < nums.length; j++) {
#                 if (i != j && nums[i] + nums[j] == target) {
#                     ints[0] = i;
#                     ints[1] = j;
#                     break a;
#                 }
#             }
#         }
#         return ints;
#     }
# }
