'''
Author: Catherine Xiong
Date: 2021-12-01 19:49:04
LastEditTime: 2021-12-01 19:49:05
LastEditors: Catherine Xiong
Description: 给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。

请你返回字符串的能量。
'''
class Solution:
    def maxPower(self, s: str) -> int:
        if not s: return 0
        max_len, cur_len = 1, 1
        cur = ''
        for x in s:
            if x != cur:
                cur = x
                max_len = max(max_len, cur_len)
                cur_len = 1
            else:
                cur_len += 1
        max_len = max(max_len, cur_len)
        return max_len