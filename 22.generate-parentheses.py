#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/24 下午6:57
@Author : Catherinexxx
@Site : 
@File : 22.generate-parentheses.py
@Software: PyCharm
"""

# 1、递归所有可能组合 再加条件筛选即可递归出合法组合 优
class Solution:
    def generateParenthesis(self, n):
        res = []
        def generate(left, right, s):
            if len(s)==2*n:
                res.append(s)
                return

            # 剪枝 做括号可以放 但数量=n 右括号只能在左括号多的时候放
            if left < n:
                generate(left+1, right, s+"(")
            if right < left:
                generate(left, right+1, s+")")
        generate(0, 0, "")
        return res

# DP
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        total_l = []
        total_l.append([None])    # 0组括号时记为None
        total_l.append(["()"])    # 1组括号只有一种情况
        for i in range(2,n+1):    # 开始计算i组括号时的括号组合
            l = []
            for j in range(i):    # 开始遍历 p q ，其中p+q=i-1 , j 作为索引
                now_list1 = total_l[j]    # p = j 时的括号组合情况
                now_list2 = total_l[i-1-j]    # q = (i-1) - j 时的括号组合情况
                for k1 in now_list1:
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2
                        l.append(el)    # 把所有可能的情况添加到 l 中
            total_l.append(l)    # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
        return total_l[n]