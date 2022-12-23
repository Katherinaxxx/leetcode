"""
Date: 2022-12-22 15:33:03
LastEditors: yhxiong
LastEditTime: 2022-12-22 16:02:29
Description: 
"""
#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
# 双指针
# 先排序 然后两端向中间逼近找0 
class Solution(object):
    def threeSum(self, nums): 
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        -2 -2 -1 0 1 2
        i  l         r

        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2): 
            # 跳过数值一样的
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: l += 1
                elif s > 0: r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # 跳过数值一样的
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res



# @lc code=end

