#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/5/22 5:49 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 剑指 Offer 59 - II. 队列的最大值.py
@Description: 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class MaxQueue:

    def __init__(self):
        self.A = collections.deque()    # 存value
        self.B = collections.deque()    # 单调 相当于max和候选max

    def max_value(self) -> int:
        return self.B[0] if self.B else -1

    def push_back(self, value: int) -> None:
        self.A.append(value)
        # 把B中所有小于value的pop掉
        while self.B and self.B[-1] < value:
            self.B.pop()
        self.B.append(value)

    def pop_front(self) -> int:
        if not self.A:return -1
        a = self.A.popleft()
        if a == self.B[0]:
            self.B.popleft()
        return a
