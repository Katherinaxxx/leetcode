'''
Author: Catherine Xiong
Date: 2022-12-28 18:31:41
LastEditTime: 2022-12-28 18:33:28
LastEditors: Catherine Xiong
Description: 
'''
#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
# @lc code=end

