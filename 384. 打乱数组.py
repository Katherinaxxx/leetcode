'''
Author: Catherine Xiong
Date: 2021-11-22 21:12:47
LastEditTime: 2021-11-22 21:12:48
LastEditors: Catherine Xiong
Description: 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。

实现 Solution class:

Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shuffle-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import random
import copy
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ori = copy.deepcopy(nums)

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.ori


    def shuffle(self):
        """
        :rtype: List[int]
        """
        L = len(self.ori)
        res = []
        cand = copy.deepcopy(self.ori)
        res = random.sample(cand, L)
        return res