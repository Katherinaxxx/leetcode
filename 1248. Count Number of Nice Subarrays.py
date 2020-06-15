#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/27 上午11:53
@Author : Catherinexxx
@Site : 
@File : 1248. Count Number of Nice Subarrays.py
@Software: PyCharm
"""
"""
给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 前缀和 O(n)time O(n)space
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        acc = cnt = 0
        d = {}
        for x in nums:
            acc += x%2==1
            if acc == k:
                cnt += 1
            # 如果中间有某些段存在
            if acc - k in d:
                cnt += d[acc-k]
            if acc not in d:
                d[acc] = 1
            else:
                d[acc] += 1
        return cnt

# 数学
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = [-1]
        ans = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                odd.append(i)
        odd.append(n)
        print(odd)
        for i in range(1, len(odd) - k):
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return ans