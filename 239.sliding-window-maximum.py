#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/10/18 下午2:48
@Author : Catherinexxx
@Site : 
@File : 239.sliding-window-maximum.py
@Software: PyCharm
"""

# # 1、暴力 O(n*k)
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         times = len(nums) - k + 1
#         l = []
#         if nums == [] or k == 0:
#             return []
#         for i in range(times):
#             a = [nums[j] for j in range(i,i+k)]
#             l.append(max(a))
#         return l

## 思路一样但是快一点 O(n*k)
# class Solution:
#     def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
#         n = len(nums)
#         if n * k == 0:
#             return []
#         return [max(nums[i:i + k]) for i in range(n - k + 1)]


# 2、deque 双端队列
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        """

        :param nums:
        :param k:
        :return:
        """
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output

# 同上 双端队列 存索引 注释更清晰
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)

        # 特判
        if size == 0:
            return []
        # 结果集
        res = []
        # 滑动窗口，注意：保存的是索引值
        window = deque()

        for i in range(size):
            # 当元素从左边界滑出的时候，如果它恰恰好是滑动窗口的最大值
            # 那么将它弹出
            if i >= k and i - k == window[0]:
                window.popleft()

            # 如果滑动窗口非空，新进来的数比队列里已经存在的数还要大
            # 则说明已经存在数一定不会是滑动窗口的最大值（它们毫无出头之日）
            # 将它们弹出
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)

            # 队首一定是滑动窗口的最大值的索引
            if i >= k - 1:
                res.append(nums[window[0]])
        return res

