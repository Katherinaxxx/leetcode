'''
Author: Catherine Xiong
Date: 2021-11-24 19:13:47
LastEditTime: 2021-11-24 19:13:48
LastEditors: Catherine Xiong
Description: 从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
"""
max - min < 5 则能构成顺子
"""
# 排序+遍历
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        joker = 0 # 非joker的index
        for i in range(4):
            if nums[i] == 0: 
                joker += 1
                continue
            if nums[i] == nums[i+1]: return False
        return nums[-1] - nums[joker] < 5

# set
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        max_, min_ = 0, 14
        repeat = set()
        for n in nums:
            if n == 0:
                continue
            if n in repeat: return False
            repeat.add(n)
            max_ = max(max_, n)
            min_ = min(min_, n)

        return max_ - min_ < 5