#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/20 上午11:49
@Author : Catherinexxx
@Site : 
@File : 438. Find All Anagrams in a String.py
@Software: PyCharm
"""
"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 遍历判断是否是异位词 O(n^2)time 超时
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         n, m = len(s), len(p)
#         res = []
#         for i in range(n-m+1):
#             if self.isAnagrams(s[i:i+m], p):
#                 res.append(i)
#         return res
#     def isAnagrams(self, s, t):
#         hash = {}
#         for i in range(len(s)):
#             if s[i] in hash:
#                 hash[s[i]] += 1
#             else:
#                 hash[s[i]] = 1
#         for i in range(len(t)):
#             if t[i] in hash:
#                 hash[t[i]] -= 1
#             else:
#                 return False
#         for v in hash.values():
#             if v!=0:
#                 return False
#         return True


# 滑动窗口 和567. Permutation in String相似
# O(n)time O(n)space
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r = 0, 0
        res = []
        from collections import Counter
        p_cnt = Counter(p)
        cur_cnt = Counter()
        while r < len(s):
            cur_cnt[s[r]] += 1
            r += 1
            while all(map(lambda x: cur_cnt[x]>=p_cnt[x], p_cnt.keys())):
                if r - l == len(p):
                    res.append(l)
                cur_cnt[s[l]] -= 1
                l += 1
        return res

# 滑窗 优化 增加了遇不到时从下一个位置开始
class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        '''
        解法1：滑动窗口
        '''
        res = []
        window = {}     # 记录窗口中各个字符数量的字典
        needs = {}      # 记录目标字符串中各个字符数量的字典
        for c in p: needs[c] = needs.get(c, 0) + 1  # 统计目标字符串的信息

        length, limit = len(p), len(s)
        left = right = 0                    # 定理两个指针，分别表示窗口的左、右界限

        while right < limit:
            c = s[right]
            if c not in needs:              # 当遇到不需要的字符时
                window.clear()              # 将之前统计的信息全部放弃
                left = right = right + 1    # 从下一位置开始重新统计
            else:
                window[c] = window.get(c, 0) + 1            # 统计窗口内各种字符出现的次数
                if right-left+1 == length:                  # 当窗口大小与目标字符串长度一致时
                    if window == needs: res.append(left)    # 如果窗口内的各字符数量与目标字符串一致就将left添加到结果中
                    window[s[left]] -= 1                    # 并将移除的字符数量减一
                    left += 1                               # left右移
                right += 1                                  # right右移
        return res
