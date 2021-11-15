'''
Author: Catherine Xiong
Date: 2020-05-08 16:53:00
LastEditTime: 2021-10-26 21:53:34
LastEditors: Catherine Xiong
Description: 
'''
"""
给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 单调栈
# O(n+m) time  O(n) space

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         stack = []
#         res = [-1] * len(nums1)
#         for a in nums2:
#             while stack and a>stack[-1]:
#                 if stack[-1] in nums1:
#                     res[nums1.index(stack.pop())] = a
#                 else:
#                     stack.pop()

#             stack.append(a)
#         return res

# 用了个hashmap来表示结果 O(n+m) time  O(m) space 运行快了一点不过仅仅是因为hashmap查询更快
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, hashmap = list(), dict() # hashmap记录了nums2中每个值的 下一个比他大的值
        for i in nums2:
            while len(stack) != 0 and stack[-1] < i:hashmap[stack.pop()] = i
            stack.append(i)
        return [hashmap.get(i,-1) for i in nums1]


