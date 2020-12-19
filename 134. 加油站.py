#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/11/18 8:25 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 134. 加油站.py
@Description: 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gas-station
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 遍历
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas): return -1
        n = len(gas)
        for i in range(n):
            if gas[i] < cost[i]: continue
            cur = 0
            flag = True
            for j in range(n):
                idx = (i + j) % n
                cur = cur + gas[idx] - cost[idx]
                if cur < 0:
                    flag = False
                    break
            if flag: return i
        return -1

# O(n) O(1) 需满足两个条件：1）总和大于消耗 2）每次剩余大于消耗
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # total记录可获得的总油量-总油耗， cur记录当前油耗情况， ans记录出发位置
        total, cur, ans = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:                     # 油不够开到i站
                cur = 0                     # cur置零，在新位置重新开始计算油耗情况
                ans = i + 1                 # 将起始位置改成i+1
        return ans if total >= 0 else -1    # 如果获得的汽油的量小于总油耗，则无法环
                                            # 行一周返回 -1；反之返回ans

