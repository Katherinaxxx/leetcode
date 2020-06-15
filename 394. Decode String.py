#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/28 上午11:47
@Author : Catherinexxx
@Site : 
@File : 394. Decode String.py
@Software: PyCharm
"""
"""
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 栈 遇到非]则入栈 遇到]后开始出 直到出到[ 栈顶必为数字弹出  即可得到一段解码的字符串 然后继续重复这个过程
# time O(s) space O(s)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            while i < len(s) and s[i] != ']':
                stack.append(s[i])
                i += 1
            # "2[abc]3[cd]ef" 最后ef这种情况
            if i == len(s) and s[i-1] != ']':
                break
            tmp = ''
            while stack[-1] != '[':
                tmp = stack.pop() + tmp
            stack.pop()
            num = ''
            # 数字不一定是一位
            while len(stack)>0 and stack[-1] in '0123456789':
                num = stack.pop() + num
            tmp = tmp * int(num)
            stack.append(tmp)
            i += 1
        return ''.join(stack)

# 别人写的栈 看着很简洁 但是我觉得没有我写的直观
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res

# 递归
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)