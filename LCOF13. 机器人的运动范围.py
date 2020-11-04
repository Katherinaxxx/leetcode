#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/10/2 上午9:52
@Author : Catherinexxx
@Site : 
@File : LCOF13. 机器人的运动范围.py
@Software: PyCharm
"""
# 数位和
def digitsum(n):
    return digitsum(n//10)+n%10 if n else 0
# O(mn)time O(mn)space
class Solution:
	def movingCount(self,m:int,n:int,k:int)->int:
		vis=set([(0,0)])
		for i in range(m):
			for j in range(n):
				if((i-1,j)in vis or(i,j-1)in vis)and digitsum(i)+digitsum(j)<=k:
					vis.add((i,j))
		return len(vis)
