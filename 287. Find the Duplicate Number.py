#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/8 下午1:49
@Author : Catherinexxx
@Site : 
@File : 287. Find the Duplicate Number.py
@Software: PyCharm
"""
"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# # hashmap O(n)time O(n)space 但是题目要求O(1)space
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         h = {}
#         for x in nums:
#             if x in h:
#                 return x
#             h[x] = 1

# 前提是n个数且在1-n这区间 二分查找 如果小于个树中位数的数目过半 说明重复的这个数一定在【1，中位数】 之后中位数=【1，中位数】的中位数 以此类推
# O(logn)*O(n)=O(nlogn)time. O(1)space
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1

        while left < right:
            mid = left + (right - left) // 2

            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            # 根据抽屉原理，小于等于 4 的数的个数如果严格大于 4 个，
            # 此时重复元素一定出现在 [1, 4] 区间里

            if cnt > mid:
                # 重复的元素一定出现在 [left, mid] 区间里
                right = mid
            else:
                # if 分析正确了以后，else 搜索的区间就是 if 的反面
                # [mid + 1, right]
                left = mid + 1
        return left

# 前提是n个数且在1-n这区间 快慢指针
# O(n)time O(1)space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # node = index of nums
        # node.next = nums[node]
        # node.next.next = nums[nums[node]]
        slow = nums[0]         #先走一步
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]] # 曾经犯的一个错误，以为这里会固定地在环入口，值相同的那个点相遇
        root = 0                    # 其实它们可以在环上任何一个node相遇，这里就是任何一个数组的下标index
        while root != slow:
            root = nums[root]
            slow = nums[slow]
        return slow             # 回到循环结束的上一步
                                # nums[proot] == nums[pslow]
                                # The last slow = nums[proot] and this value at least has two slot in the array

