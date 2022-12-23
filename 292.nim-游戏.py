"""
Date: 2022-12-23 14:57:47
LastEditors: yhxiong
LastEditTime: 2022-12-23 15:06:26
Description: 
"""
#
# @lc app=leetcode.cn id=292 lang=python
#
# [292] Nim 游戏
#

# @lc code=start
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 3:
            return True
        new_size = n + 1
        memo = [False] * (new_size)
        
        for i in range(4): 
            memo[i] = True
        
        for i in range(4,new_size):
            for j in range(1,4):
                if memo[i] == True:
                    break
                if memo[i-j] == True:
                    memo[i] = False
                else:
                    memo[i] = True
        
        return memo[n]
# @lc code=end

