#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/7/13 10:26 PM
@Author : Catherinexxx
@File : 剑指 Offer 30. 包含min函数的栈.py
@Description: 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)


    def pop(self) -> None:
        if self.stack.pop() == self.minstack[-1]:
            self.minstack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def min(self) -> int:
        return self.minstack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()