"""
Date: 2022-12-23 15:39:50
LastEditors: yhxiong
LastEditTime: 2022-12-23 15:43:58
Description: 
"""
#
# @lc app=leetcode.cn id=136 lang=python
#
# [136] 只出现一次的数字
#

# @lc code=start
# 1 暴力遍历两次 O(n^2)
# 2 排序 时O(nlogn) 空O(n) 不满足要求
# 3 异或 中间重复的会抵消  O(n)
class Solution:
    def singleNumber(self, nums):
        res = 0
        for i in nums:
            res ^= i
        return res
# @lc code=end

