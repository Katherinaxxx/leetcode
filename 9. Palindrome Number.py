#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/10 上午11:39
@Author : Catherinexxx
@Site : 
@File : 9. Palindrome Number.py
@Software: PyCharm
"""
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 倒序后比较 O(nlogn)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
# 两端往中间 O(n)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        s = str(x)
        i, j = 0, len(s)-1
        while i < j :
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True
# 不转字符串
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        只反转后面一半的数字!!(节省一半的时间)
        """
        if x < 0 or (x!=0 and x%10==0):
            return False
        elif x == 0:
            return True
        else:
            import math
            length = int(math.log(x, 10)) + 1
            reverse_x = 0
            # 构造后面一半反转 和 前面一半
            for i in range(length//2):
                remainder = x % 10
                x = x // 10
                reverse_x = reverse_x * 10 + remainder
            # 当x为奇数时, 只要满足 reverse_x == x//10 即可
            if reverse_x == x or reverse_x == x//10:
                return True
            else:
                return False