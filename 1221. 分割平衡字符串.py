'''
Author: Catherine Xiong
Date: 2021-09-07 19:50:39
LastEditTime: 2021-09-07 19:54:21
LastEditors: Catherine Xiong
Description: 在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。

给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

注意：分割得到的每个字符串都必须是平衡字符串。

返回可以通过分割得到的平衡字符串的 最大数量 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-a-string-in-balanced-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 有点类似括号匹配，只不过括号用的栈。这个比较简单，计数即可
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        nums = 0
        res = 0
        for x in s:
            if x == "R":
                nums += 1
            else:
                nums -= 1
            if nums == 0:
                res += 1
                nums = 0
        return res