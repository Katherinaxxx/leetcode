"""
Date: 2022-12-23 09:54:31
LastEditors: yhxiong
LastEditTime: 2022-12-23 10:16:00
Description: 
"""
#
# @lc app=leetcode.cn id=258 lang=python
#
# [258] 各位相加
#

# @lc code=start
# 不使用循环或者递归，在 O(1) 时间复杂度
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0 : return 0
        if num % 9 == 0 : return 9
        else : return (num % 9)
# @lc code=end

