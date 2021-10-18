'''
Author: Catherine Xiong
Date: 2021-08-30 22:03:58
LastEditTime: 2021-08-30 23:19:47
LastEditors: Catherine Xiong
Description: 
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s) + 1, len(p) + 1
        dp = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                # 分成空正则和非空正则两种
                if j == 0:
                    dp[i][j] = i == 0
                else:
                    # 非空正则分为两种情况 * 和 非*
                    if p[j-1] != '*':
                        if i>0 and (s[i-1] == p[j-1] or p[j-1] == "."):
                            dp[i][j] = dp[i-1][j-1]
                    else:
                        # 碰到 * 了，分为看和不看两种情况
                        # 不看
                        if j >= 2:
                            dp[i][j] |= dp[i][j - 2]
                        # 看
                        if i >= 1 and j >= 2 and (s[i-1]==p[j-2] or p[j-2] == "."):
                            dp[i][j] |= dp[i - 1][j]
        return dp[n-1][m-1]
