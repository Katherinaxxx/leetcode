#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/5/11 10:26 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 1734. 解码异或后的排列.py
@Description: 给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。

它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。比方说，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。

给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-xored-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)
        res = []

        ABCDE = 0   # 所有数异或
        for i in range(1,n+2):
            ABCDE^=i

        BCDE = 0    # 除第一个之外的异或
        for i in range(1,n,2):
            BCDE^=encoded[i]
        A = BCDE^ABCDE  # 找到第一个数之后 转化成leetcode1720

        res.append(A)
        for i in range(n):
            res.append(res[-1]^encoded[i])
        return res

