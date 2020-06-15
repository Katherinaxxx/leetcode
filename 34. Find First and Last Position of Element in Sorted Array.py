#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/20 下午2:49
@Author : Catherinexxx
@Site : 
@File : 34. Find First and Last Position of Element in Sorted Array.py
@Software: PyCharm
"""
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 直接的想法 先排除特例 之后看是否存在这个值 更新start、end 最后再处理一下 O(n)time
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:

#         if not nums or target < nums[0] or target > nums[-1]:
#             return [-1, -1]
#         start, end = float("inf"), float("-inf")
#         for i, v in enumerate(nums):
#             if v == target and i < start:
#                 start = i
#             elif v == target and i > end:
#                 end = i
#         if start < float("inf") and end == float("-inf"):
#             end = start
#         return [start, end] if start!= float("inf") else [-1, -1]

# 二分查找 O(logn)time
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 分两次查找
        low = 0
        high = len(nums) - 1
        res = []
        #寻找左边界
        while low <= high:
            mid = (low+high) >> 1
            if nums[mid] == target:
                # 判断是否是起点 若是则计入结果并推出循环
                if mid == 0 or nums[mid-1] != target:
                    res.append(mid)
                    break
                else:
                    high = mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        # 若不存在起点 则可以直接返回了
        if not res:
            return [-1,-1]
        #寻找右边界
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high) >> 1
            if nums[mid] == target:
                # 判断是否是终点
                if (mid == len(nums) - 1) or nums[mid+1] != target:
                    res.append(mid)
                    break
                else:
                    low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return res