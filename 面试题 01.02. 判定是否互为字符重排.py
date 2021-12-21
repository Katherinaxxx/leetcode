'''
Author: Catherine Xiong
Date: 2021-12-16 20:46:37
LastEditTime: 2021-12-16 20:50:28
LastEditors: Catherine Xiong
Description: 给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
'''
# time O(n) space O(n)
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        from collections import defaultdict
        dic = defaultdict(int)
        for s in s1:
            dic[s] += 1
        for s in s2:
            dic[s] -= 1
        for s, v in dic.items():
            if v != 0: return False
        return True
