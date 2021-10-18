'''
Author: Catherine Xiong
Date: 2021-10-12 19:27:09
LastEditTime: 2021-10-12 19:27:11
LastEditors: Catherine Xiong
Description: 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
'''
# 排序 O(nlogn)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n**2 for n in nums])
# 双指针 两端是最大 O(n) 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        i, j, pos = 0, len(nums) - 1, len(nums) - 1
        while i <= j:
            if nums[i]**2 > nums[j]**2:
                res[pos] = nums[i]**2
                i += 1
            else:
                res[pos] = nums[j] ** 2
                j -= 1
            pos -= 1
        return res
