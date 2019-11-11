#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/4 下午4:07
@Author : Catherinexxx
@Site : 
@File : 874. Walking Robot Simulation.py
@Software: PyCharm
"""

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 初始朝北走 dy +1、 dx 0
        dx, dy, x, y = 0, 1, 0, 0
        distance = 0
        # obstacles hash
        obs_dict = {}
        for obs in obstacles:
            obs_dict[tuple(obs)] = 0
        for com in commands:
            # 左转
            if com == -2:
                dx, dy = -dy, dx
            # 右转
            elif com == -1:
                dx, dy = dy, -dx
            else:
                for j in range(com):
                    next_x = x + dx
                    next_y = y + dy
                    if (next_x, next_y) in obs_dict:
                        break
                    x, y = next_x, next_y
                    distance = max(distance, x*x + y*y)
        return distance
