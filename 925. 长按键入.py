#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/10/21 下午8:05
@Author : Catherinexxx
@Site : 
@File : 925. 长按键入.py
@Software: PyCharm
"""
"""
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/long-pressed-name
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 双指针
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while i < len(name):
            if j == len(typed): return False
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        return True if typed[j:] == name[-1]*(len(typed)-j) else False