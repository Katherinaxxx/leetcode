'''
Author: Catherine Xiong
Date: 2021-11-15 19:33:49
LastEditTime: 2021-11-15 19:33:49
LastEditors: Catherine Xiong
Description: 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
'''
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)

