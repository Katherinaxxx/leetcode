#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/10 下午12:26
@Author : Catherinexxx
@Site : 
@File : 125. Valid Palindrome.py
@Software: PyCharm
"""
"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。
"""
# 正则 把非数字字母的换成'' 并全转为小写 然后判断 O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
            tmp = re.sub(r"[^A-Za-z0-9]","", s).lower()
            return tmp == tmp[::-1]



# 双指针 O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
            n = len(s)
            left = 0
            right = n - 1
            while left < right:
                while left < right and not s[left].isalnum():
                    left += 1
                while left < right and not s[right].isalnum():
                    right -= 1
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
            return True