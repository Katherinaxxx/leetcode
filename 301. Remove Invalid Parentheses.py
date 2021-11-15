'''
Author: Catherine Xiong
Date: 2020-05-22 14:59:57
LastEditTime: 2021-10-27 21:08:43
LastEditors: Catherine Xiong
Description: 
'''
"""
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
"""


# BFS 如果我们每次只删除一个括号，然后观察被删除一个括号后是否合法，如果已经合法了，我们就不用继续删除了啊
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s: str) -> bool:
            cnt = 0
            for c in s:
                if c == "(":
                    cnt += 1
                elif c == ")":
                    cnt -= 1
                if cnt < 0: return False  # 只用中途cnt出现了负值，你就要提前终止循环，已经出现非法字符了
            return cnt == 0

        # BFS
        level = {s}
        while True:
            valid = list(filter(isValid, level))  # 所有合法字符都筛选出来
            if valid: return valid  # 如果当前valid是非空的，说明已经有合法的产生了

            # 如果没有有效的 则进入下一层level
            next_level = set()  # 用set避免重复
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":  # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i] + item[i + 1:])
            level = next_level

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        @lru_cache(None)
        def dfs(i, l):
            if l < 0: return []  # 左括号不够，一定无效
            if i == len(s): return [""] if l == 0 else []  # i 遍历结束时，l为0才有效，否则无效

            if s[i] in "()":
                ans = dfs(i+1, l) + [s[i] + x for x in dfs(i+1, l+(1 if s[i]=="(" else -1))]
                return list(set(x for x in ans if len(x)==max(map(len, ans))))  # 取最长的几个并去重
            return [s[i] + x for x in dfs(i+1, l)]  # 检测到非括号，接着往下走即可

        return dfs(0, 0)

