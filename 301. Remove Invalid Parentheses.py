#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/22 下午2:59
@Author : Catherinexxx
@Site : 
@File : 301. Remove Invalid Parentheses.py
@Software: PyCharm
"""
"""
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
"""


# BFS 如果我们每次只删除一个括号，然后观察被删除一个括号后是否合法，如果已经合法了，我们就不用继续删除了啊
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s: str) -> bool:
            cnt = 0
            for c in s:
                if c == "(":
                    cnt += 1
                elif c == ")":
                    cnt -= 1
                if cnt < 0: return False  # 只用中途cnt出现了负值，你就要提前终止循环，已经出现非法字符了
            return cnt == 0

        # BFS
        level = {s}
        while True:
            valid = list(filter(isValid, level))  # 所有合法字符都筛选出来
            if valid: return valid  # 如果当前valid是非空的，说明已经有合法的产生了

            # 如果没有有效的 则进入下一层level
            next_level = set()  # 用set避免重复
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":  # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i] + item[i + 1:])
            level = next_level
