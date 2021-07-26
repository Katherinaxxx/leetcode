#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/6/29 7:50 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 168. Excel表列名称.py
@Description: 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。


"""
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            columnNumber -= 1
            ans = chr(columnNumber%26+65) + ans
            columnNumber //= 26
        return ans