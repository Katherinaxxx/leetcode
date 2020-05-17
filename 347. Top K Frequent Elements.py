#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/11 下午8:39
@Author : Catherinexxx
@Site : 
@File : 347. Top K Frequent Elements.py
@Software: PyCharm
"""
# # 库函数
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         return [i[0] for i in Counter(nums).most_common(k)]

# 堆排序
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        heap_max = []
        dic_fre = {}
        ans = []
        for i in nums:
            if i in dic_fre:
                dic_fre[i]+=1
            else:
                dic_fre[i] = 1
        # 放入大顶堆
        for i in dic_fre:
            heapq.heappush(heap_max,(-dic_fre[i],i))
        # 取出前k个
        for j in range(k):
            p = heapq.heappop(heap_max)
            ans.append(p[1])
        return ans
