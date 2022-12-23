"""
Date: 2022-12-22 16:04:46
LastEditors: yhxiong
LastEditTime: 2022-12-22 16:10:42
Description: 
"""
#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f1, f2 = 1, 2
        if n <= 3: return n
        for i in range(3, n+1):
            f1, f2 = f2, f1 + f2
        return f2
# @lc code=end

