#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/5/11 10:24 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 1720. 解码异或后的数组.py
@Description: 未知 整数数组 arr 由 n 个非负整数组成。

经编码后变为长度为 n - 1 的另一个整数数组 encoded ，其中 encoded[i] = arr[i] XOR arr[i + 1] 。例如，arr = [1,0,2,1] 经编码后得到 encoded = [1,2,3] 。

给你编码后的数组 encoded 和原数组 arr 的第一个元素 first（arr[0]）。

请解码返回原数组 arr 。可以证明答案存在并且是唯一的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-xored-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 异或运算满足交换律和结合律；
# 任意整数和自身做异或运算的结果都等于 0
# 任意整数和 0 做异或运算的结果都等于其自身
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for num in encoded:
            arr.append(arr[-1] ^ num)
        return arr