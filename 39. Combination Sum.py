#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/4/30 下午6:38
@Author : Catherinexxx
@Site : 
@File : 39. Combination Sum.py
@Software: PyCharm
"""
'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 递归 回溯
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def recursion(cur, candidates):
            if sum(cur) == target:
                res.append(cur[:])
                return
            # 剪枝
            if sum(cur) > target:
                return
            for i in range(len(candidates)):
                cur.append(candidates[i])
                recursion(cur, candidates[i:])
                cur.pop()                       # traceback
        recursion([], candidates)
        return res