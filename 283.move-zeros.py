'''
Author: Catherine Xiong
Date: 2020-11-19 22:10:44
LastEditTime: 2021-10-14 19:14:05
LastEditors: Catherine Xiong
Description: 
'''

# python


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i],nums[j]
                j += 1


# 双指针 i遇0 则j从j后找到第一个不为0的 交换 然后i=j j继续往后找
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            j = i + 1
            while j < len(nums) and nums[j] == 0:
                j += 1
            if i < len(nums) and j < len(nums):
                nums[i], nums[j] = nums[j], nums[i]


# // java
# class Solution {
#     public void moveZeroes(int[] nums) {
#         int j = 0;
#         for (int i = 0; i < nums.length; ++i) {
#             if (nums[i] != 0) {
#                 nums[j] = nums[i];
#                 if (i != j) {
#                     nums[i] = 0;
#                 }
#                 j++;
#             }
#         }
#     }
# }