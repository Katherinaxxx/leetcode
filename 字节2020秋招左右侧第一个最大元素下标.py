#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/9/6 下午7:49
@Author : Catherinexxx
@Site : 
@File : 字节2020秋招左右侧第一个最大元素下标.py
@Software: PyCharm
"""

def get_answer(nums):
    i=0
    stack=[]
    res=0
    while i<len(nums):
        if not stack or nums[stack[-1]]>=nums[i]:
            stack.append(i)
        else:
            while stack and nums[stack[-1]]<nums[i]:
                val=stack.pop()
                if not stack:
                    left=0
                else:
                    left=stack[-1]+1
                right=i+1
                res=max(res,left*right)
            stack.append(i)
        i+=1
    return res