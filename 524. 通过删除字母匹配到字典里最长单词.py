'''
Author: Catherine Xiong
Date: 2021-09-14 20:02:02
LastEditTime: 2021-09-14 20:21:46
LastEditors: Catherine Xiong
Description: 给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。

如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 排序+匹配
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # 先按长度降序，再按照字典序升序
        dictionary.sort(key=lambda x: (-len(x), x))
        for d in dictionary:
            i = 0
            for c in s:
                if c == d[i]:
                    i += 1
                if i == len(d):
                    return d 
        return ''