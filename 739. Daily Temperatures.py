#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/8 下午3:46
@Author : Catherinexxx
@Site : 
@File : 739. Daily Temperatures.py
@Software: PyCharm
"""
"""
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# # 从后往前遍历  O(n^2)time O(n)space 果不其然超时了
# # res[i] 表示未来等待几天可以超过第i天的温度
# # 若i以后没有比他大的则继续
# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         res = [0] * len(T)
#         for i in range(len(T)-2, -1, -1):
#             for j in range(i+1, len(T)):
#                 if T[j] > T[i]:
#                     res[i] = j-i
#                     break
#         return res

# stack 单调栈 找到一个数后 要找出在他之后更大的一个数
# O(n) time  O(n) space
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)

        for idx, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                # 当stack为空时，运行stack.append(idx)，则stack=[0]
                # 然后仅当遍历元素 t 小于stack顶端的值时append进去，
                # 这会导致stack中idx代表的元素是单调递减的，
                # 如果此时遍历到一个 t，大于stack顶端的值，那这个t就是离stack
                # 顶端值最近的那个大值。
                res[stack.pop()] = idx-stack[-1]
                # 然后pop出来，还是要注意stack.pop出来的是idx，这样res这
                # 一串0里对应位置的0就会被替换成应有的值。
                # 再进入while循环判断t和stack.pop后的新的顶端值哪个大。
                # 如此反复。
            stack.append(idx)
        return res
