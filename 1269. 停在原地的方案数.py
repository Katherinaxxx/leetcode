#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/5/13 10:37 AM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 1269. 停在原地的方案数.py
@Description: 有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。

每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。

给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。

由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/solution/python-ji-yi-hua-dfs-by-qubenhao-0jd6/
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @lru_cache(None)
        def dfs(cur, s):
            if cur == -1 or cur == arrLen or cur > s:
                return 0
            if cur <= 1 and s == 1:
                return 1
            s -= 1
            return dfs(cur, s) + dfs(cur-1,s) + dfs(cur+1,s)

        return dfs(0, steps) % (10 ** 9 + 7)
