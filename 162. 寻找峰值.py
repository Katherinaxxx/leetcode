'''
Author: Catherine Xiong
Date: 2021-09-15 21:04:22
LastEditTime: 2021-09-15 21:11:24
LastEditors: Catherine Xiong
Description: 峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-peak-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 1. 逻辑遍历
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = 0
        while i < len(nums) :
            if i < len(nums)-1 and nums[i] < nums[i+1]:
                i += 1
            elif i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 2
            # 右边小或不存在
            else:
                # 左边小或不存在
                if i==0 or nums[i] > nums[i-1]:
                    return i 
                else:
                    i += 2
        return ''

# 2. 二分法 题目说了左右无穷是负无穷，因此只要沿着递增的方向，一定存在峰值
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i+j)//2
            if nums[mid] < nums[mid+1]:
                i = mid + 1
            else:
                j = mid
        return i