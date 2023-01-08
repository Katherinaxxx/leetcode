'''
Author: Catherine Xiong
Date: 2022-12-28 18:34:16
LastEditTime: 2022-12-28 18:38:32
LastEditors: Catherine Xiong
Description: 
'''
#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
# @lc code=end

