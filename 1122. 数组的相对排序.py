#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/11/14 7:52 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 1122. 数组的相对排序.py
@Description: 给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。
未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-sort-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 库函数
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2 += sorted(set(arr1) - set(arr2))
        res = sorted(arr1, key=arr2.index)
        return res

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted(arr1, key=(arr2 + sorted(set(arr1) - set(arr2))).index)

    # 计数排序 O(n+m)time O(n)space
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        bins = [0 for _ in range(1001)]
        res = []
        for i in arr1:
            bins[i] += 1
        for i in arr2:
            res += [i] * bins[i]
            bins[i] = 0
        for i in range(len(bins)):
            res += [i] * bins[i]

        return res
