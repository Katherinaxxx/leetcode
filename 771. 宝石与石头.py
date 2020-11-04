#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/10/2 上午9:50
@Author : Catherinexxx
@Site : 
@File : 771. 宝石与石头.py
@Software: PyCharm
"""
"""
给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jewels-and-stones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# hash O(n)time O(n)space
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        lookup = {}
        for x in J:
            lookup[x] = 1
        res = 0
        for x in S:
            if x in lookup:
                res += 1
        return res
    # O(n)time O(1) space
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(map(lambda x : x in J , S))