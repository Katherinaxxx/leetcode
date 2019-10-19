#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/18 上午10:58
@Author : Catherinexxx
@Site : 
@File : 20.valid-parentheses.py
@Software: PyCharm
"""

# 1、暴力：不断replace匹配的括号 O(n^2)
# 2、栈
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "]": "[", "}": "{"}     # 右 -> 左
        stack = []        # 存左括号
        for char in s:
            if char in dic:     # 判断是否为右
                top = stack.pop() if stack else '#'     # 防止stack为空
                if dic[char] != top:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0