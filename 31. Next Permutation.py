#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/21 下午1:31
@Author : Catherinexxx
@Site : 
@File : 31. Next Permutation.py
@Software: PyCharm
"""
"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 从倒数第二往前遍历 找到他后面最小的比他大的数 交换位置 后面升序
# O(n) O(n)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                subNums = sorted(nums[i:len(nums)])
                for j in subNums:
                    if j>nums[i-1]:
                        newSub=j
                        break
                k = nums.index(newSub,i)
                nums[i-1],nums[k] = nums[k],nums[i-1]
                nums[i:] = sorted(nums[i:])
                return nums
        return nums.sort()

# O(n) O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        答题思路：从后往前寻找第一个升序对(i,j)即nums[i]<nums[j] 再从后往前找第一个大于nums[i]的数即为大数，交换着两个元素即将大数换到前面，然后将大数后面的部分倒序
        """
        n = len(nums)
        if n < 2: return nums
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:  # 要是前者大于等于后者 则不是要调整的目标 继续前移  ！第一遍出错就是这儿没有等于
            i -= 1
        if i == 0:  # 此数为最大数（之前写的 i==0 and nums[i]==max(nums)，判断冗余，现删除）
            return nums.reverse()
        else:
            j = n - 1
            while j > i - 1 and nums[j] <= nums[i - 1]:
                j -= 1
            # 交换
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            # 后面倒序
            for k in range((n - i) // 2):
                nums[i + k], nums[n - 1 - k] = nums[n - 1 - k], nums[i + k]
