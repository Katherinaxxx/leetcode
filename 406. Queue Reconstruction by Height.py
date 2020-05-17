#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/11 下午9:21
@Author : Catherinexxx
@Site : 
@File : 406. Queue Reconstruction by Height.py
@Software: PyCharm
"""
"""
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 插入排序, 身高从高到低, 每次取最高的插入结果, 则结果里所有元素都比新的元素高, 所以可直接把新的元素插入其x[1]记录的index处
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))

        res = []
        for i in people:
            res.insert(i[1], i)
        return res
