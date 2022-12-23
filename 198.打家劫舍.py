"""
Date: 2022-12-23 16:24:34
LastEditors: yhxiong
LastEditTime: 2022-12-23 16:44:13
Description: 
"""
#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        2 3 4
        走到4时只需比较2+4和3谁大
        """
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last + num, now)

        return now
# @lc code=end

