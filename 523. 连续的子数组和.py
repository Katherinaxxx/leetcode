#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/6/2 1:03 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 523. 连续的子数组和.py
@Description: 给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：

子数组大小 至少为 2 ，且
子数组元素总和为 k 的倍数。
如果存在，返回 true ；否则，返回 false 。

如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/continuous-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 遍历 O(n^2)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2: return False
        for i in range(1, len(nums)):
            for j in range(0, i):
                if sum(nums[j:i+1]) % k == 0:
                    return True
        return False
# 前缀和 O(n) 由于sum维护的是前i项的和(包括i), 这样才能保证每次count的时候, set中只含有前i - 2的和, 满足题目「长度至少为2」的条件。
# 【当两个前缀和*关于模 k 同余*时，它们的差值就是满足条件的子数组和】
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modeset = set()
        presum = 0
        for num in nums:
            presum += num
            if (presum % k) in modeset:
                return True
            modeset.add((presum - num)% k)
        return False