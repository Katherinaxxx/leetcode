#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/5/26 11:27 AM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 1190. 反转每对括号间的子串.py
@Description: 给出一个字符串 s（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 不应 包含任何括号。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 栈 O(n) O(n)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        for x in s:
            if x == '(':
                stack.append("")
            elif x == ')':
                reverse = stack.pop()[::-1]
                stack[-1] += reverse
            else:
                stack[-1] += x
        return stack[0]

class Solution(object):
    def reverseParentheses(self, s):
        while '(' in s:
            s = re.sub(r'\(([^()]*)\)', lambda x:x.group(1)[::-1], s)
        return s