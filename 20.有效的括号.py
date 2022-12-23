"""
Date: 2022-12-23 15:24:45
LastEditors: yhxiong
LastEditTime: 2022-12-23 15:30:51
Description: 
"""
#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {
            ']': '[', 
            '}': '{',
            ')': '('
        }
        stack = []
        for char in s:
            if char in dic:
                if not stack: return False
                bottom = stack.pop()
                if bottom != dic[char]:
                    return False
            else:
                stack.append(char)
        return stack == []
# @lc code=end

