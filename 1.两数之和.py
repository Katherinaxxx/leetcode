"""
Date: 2022-12-15 11:02:31
LastEditors: yhxiong
LastEditTime: 2022-12-19 14:19:33
Description: 
"""
#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            t = target - num
            if t in dic: 
                return [i, dic[t]]
            else:
                dic[num] = i
# @lc code=end

