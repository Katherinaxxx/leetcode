#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/8/17 11:09 PM
@Author : Catherinexxx
@File : 551. 学生出勤记录 I.py
@Description: 
"""
class Solution:
    def checkRecord(self, s: str) -> bool:
        return ("LLL" not in s ) and s.count("A")<2