#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/25 下午2:18
@Author : Catherinexxx
@Site : 
@File : 面试题 17.16. The Masseuse LCCI.py
@Software: PyCharm
"""

"""
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-masseuse-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# DP 当前最大的在两种之间取最大值： 当前不选 或者上次的+当前 O(n)time O(1)space

class Solution:
    def massage(self, nums: List[int]) -> int:
        last,now=0,0
        for num in nums:
            last,now=now,max(last+num,now)
        return now