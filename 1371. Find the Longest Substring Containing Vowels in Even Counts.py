#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/5/27 下午12:50
@Author : Catherinexxx
@Site : 
@File : 1371. Find the Longest Substring Containing Vowels in Even Counts.py
@Software: PyCharm
"""
"""
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。
"""

# 位运算来表示奇偶
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dp = [-float('inf')]*32
        dp[0] = -1
        pattern = 0
        res = 0
        for i in range(len(s)):
            if s[i] == 'a':
                pattern^= (1<<0)
            elif s[i] == 'e':
                pattern^= (1<<1)
            elif s[i] == 'i':
                pattern^= (1<<2)
            elif s[i] == 'o':
                pattern^= (1<<3)
            elif s[i] == 'u':
                pattern^= (1<<4)
            if dp[pattern] != -float('inf'):
                cur_len = i-dp[pattern]
                res = max(res,cur_len)
            else:
                dp[pattern] = i
        return res

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        pattern = 'aeiou'
        status  =  00000
        position = [-1] * (1<<5) # 字母出现的下标>=0, 用-1标记是不是第一次出现
        position[0] = 0          # 最大的状态等于11111, 100000正好多出一位给初始状态
        #初始状态，s[0] 对应的状态：'aeiou'都出现了0次，所以indexOf(status==0) = 0
        #细节：这里记录的是状态值之后那个字母的坐标
        #考虑一个例子elee
        # positon[0] = 0
        # position[status(e)] = 1， ans = 0, status = 01000
        # position[status(el)] = 1，ans = 1-1+1, status = 01000
        # position[status(ele)] = position[0] = 0， ans= 2-0+1, status = 00000
        # positon[status(elee)] = position[e] = 1， ans = 3-1+1, status = 01000
        # 仅在状态第一次出现时记录坐标， 之后出现仅计算长度
        res = 0
        for i in range(len(s)):
            try:
                index = pattern.index(s[i])
                status ^= (1 << index)
            except ValueError: pass
            if (p := position[status]) >= 0: # if p := position[status] >= 0: 忘记加括号，弄了好久~
                res = max(res, i-p+1)
            else:
                position[status] = i+1 #只记录第一次出现该状态时的坐标
        return res

# 前缀和
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # bit_mask由左至右对应 aeiou 5个元音字母的出现次数的奇偶性，
        # 1代表某个字母出现奇数次，0代表出现偶数次
        bit_mask = eval('0b00000')
        # 下面一行，初始化状态集，一开始元音字母都是0次(都为偶数)，这种情况发生在-1位置，即0位置的左侧
        # state_first_idx的含义为，某种状态(key)：第一次出现的位置(index)
        state_first_idx = {eval('0b00000'): -1}
        vowels = 'aeiou'
        ans = 0
        for i in range(len(s)):
            if (idx := vowels.find(s[i])) > -1:  # str的find方法，找不到返回-1，找到返回元素在字符串中的index，将找到的结果放在idx中
                bit_mask ^= eval('0b10000') >> idx  # 找到idx后，就要将对应位置进行翻转(用异或实现)
                                                    # eval('0b10000') >> idx，就是将找到的元音所对应的那位设为1，
                                                    # 它再和原始的 bit_mask 异或就实现了将元音对应位置翻转
            if bit_mask not in state_first_idx:  # 如果当前状态没有出现，则将其记录
                state_first_idx[bit_mask] = i
            ans = max(ans, i - state_first_idx[bit_mask])  # 更新结果
        return ans