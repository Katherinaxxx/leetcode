"""
Date: 2022-12-19 14:48:01
LastEditors: yhxiong
LastEditTime: 2022-12-19 16:22:53
Description: 
"""
#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, res, lookup = -1, 0, {}      # 下标很重要
        for idx, val in enumerate(s):
            # 当前字符出现过
            if val in lookup and lookup[val] > start:
                start = lookup[val]
                lookup[val] = idx
            # 当前字符没出现过
            else:
                lookup[val] = idx
                res = max(res, idx - start)
        return res
# @lc code=end

