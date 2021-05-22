#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/5/21 11:36 AM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 692. 前K个高频单词.py
@Description:
给一非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
"""
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        rereturn [x[0] for x in heapq.nsmallest(k, collections.Counter(words).items(), key=lambda a: (-a[1], a[0]))]