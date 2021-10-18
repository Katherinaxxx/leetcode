'''
Author: Catherine Xiong
Date: 2021-09-23 22:02:15
LastEditTime: 2021-09-23 22:03:51
LastEditors: Catherine Xiong
Description: 给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-three
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 递归
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n >= 1:
            if n % 3 == 0:
                return self.isPowerOfThree(n/3)
            else:
                return n == 1
        return False
            
# 迭代
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n and n % 3 == 0:
            n /=  3
        return n == 1