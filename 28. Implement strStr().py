#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/6/16 上午6:45
@Author : Catherinexxx
@Site : 
@File : 28. Implement strStr().py
@Software: PyCharm
"""
"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 滑窗法 右边先增至needle存在 左边减 O(n^2)time 超时
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, flag = 0, False
        for i in range(len(needle) - 1, len(haystack)):
            while needle in haystack[:i]:
                flag = True
                l += 1
        return -1 if not flag else l - 1


# sunday O(mn)time
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Func: 计算偏移表
        def calShiftMat(st):
            dic = {}
            for i in range(len(st) - 1, -1, -1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st) - i
            dic["ot"] = len(st) + 1
            return dic

        # 其他情况判断
        if len(needle) > len(haystack): return -1
        if needle == "": return 0

        # 偏移表预处理
        dic = calShiftMat(needle)
        idx = 0

        while idx + len(needle) <= len(haystack):

            # 待匹配字符串
            str_cut = haystack[idx:idx + len(needle)]

            # 判断是否匹配
            if str_cut == needle:
                return idx
            else:
                # 边界处理
                if idx + len(needle) >= len(haystack):
                    return -1
                # 不匹配情况下，根据下一个字符的偏移，移动idx
                cur_c = haystack[idx + len(needle)]
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic["ot"]

        return -1 if idx + len(needle) >= len(haystack) else idx

# kmp O(n+m)
class Solution:
    def strStr(self,s: str,p: str) -> int:
        i,j = 0,0
        m,n = len(s), len(p)
        nxt = self.nxt_pos(p)
        while i<m and j<n:
            # 注意 一定要有j=-1
            if j==-1 or s[i]==p[j]:
                i+=1
                j+=1
            else:
                j=nxt[j]
        return i-n if j==n else -1
    # next[i]表示p的前i个字符组成的子串p[0,..,i-1]的最长公共前后缀长度
    def nxt_pos(self, p):
        n=len(p)
        nxt = [-1]+[0]*n
        for i in range(2,n+1):
            j=nxt[i-1]
            while p[i-1]!=p[j] and j!=-1: #注意 是and
                j=nxt[j]
            nxt[i]=j+1
        return nxt
