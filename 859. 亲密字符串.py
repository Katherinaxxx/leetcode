'''
Author: Catherine Xiong
Date: 2021-11-23 19:31:56
LastEditTime: 2021-11-23 19:31:56
LastEditors: Catherine Xiong
Description: 给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。

交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。

例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/buddy-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
"""
1.字符串长度不相等, 直接返回false
2.字符串相等的时候, 只要有重复的元素就返回true
3.A, B字符串有不相等的两个地方, 需要查看它们交换后是否相等即可.
"""
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        diff = []
        if len(goal) != len(s): return False
        if s == goal and len(set(s)) < len(s): return True
        for i in range(len(goal)):
            if goal[i] != s[i]:
                diff.append([s[i], goal[i]])
        if len(diff) == 2 and diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]:
            return True
        
        return False 
