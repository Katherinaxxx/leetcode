#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/2/20 下午1:23
@Author : Catherinexxx
@Site : 
@File : LCOF9用两个栈实现队列.py
@Software: PyCharm
"""


# # 一个栈
# class CQueue:

#     def __init__(self):
#         self.queue = []
#         self.head = None


#     def appendTail(self, value: int) -> None:
#         self.queue.append(value)
#         if len(self.queue) == 1:
#             self.head = value


#     def deleteHead(self) -> int:
#         if not self.queue:
#             return -1
#         else:
#             self.head = None if len(self.queue) == 1 else self.queue[1]
#             return self.queue.pop(0)

# 两个栈 A进 B倒装
class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()