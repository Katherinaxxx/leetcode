'''
Author: Catherine Xiong
Date: 2021-11-24 18:50:38
LastEditTime: 2021-11-24 18:53:16
LastEditors: Catherine Xiong
Description: 给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。
'''
"""
1. 统计字母可能出现在哪些数字中
2. 经过对比，02468唯一；357与646相关；19与。。。
3. 统计字母出现次数，按照以上逻辑计算即可

"""
class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)

        cnt = [0] * 10
        cnt[0] = c["z"]
        cnt[2] = c["w"]
        cnt[4] = c["u"]
        cnt[6] = c["x"]
        cnt[8] = c["g"]

        cnt[3] = c["h"] - cnt[8]
        cnt[5] = c["f"] - cnt[4]
        cnt[7] = c["s"] - cnt[6]
        
        cnt[1] = c["o"] - cnt[0] - cnt[2] - cnt[4]

        cnt[9] = c["i"] - cnt[5] - cnt[6] - cnt[8]

        return "".join(str(x) * cnt[x] for x in range(10))
