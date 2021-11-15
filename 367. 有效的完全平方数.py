'''
Author: Catherine Xiong
Date: 2021-11-04 22:07:50
LastEditTime: 2021-11-04 22:07:50
LastEditors: Catherine Xiong
Description: 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

进阶：不要 使用任何内置的库函数，如  sqrt 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-perfect-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def isPerfectSquare1(self, num: int) -> bool:
        cnt = 1
        while num > 0:
            num -= 2*cnt-1
            cnt+=1
        return num == 0


    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1
        right = num
        while left < right:
            mid = (left + right) // 2
            N = mid*mid
            if N == num:
                return True
            elif N < num:
                left = mid + 1
            else:
                right = mid - 1
        return left * left == num