'''
Author: Catherine Xiong
Date: 2021-12-02 19:41:38
LastEditTime: 2021-12-02 19:42:02
LastEditors: Catherine Xiong
Description: 给你一个长度为 n 的整数数组 score ，其中 score[i] 是第 i 位运动员在比赛中的得分。所有得分都 互不相同 。

运动员将根据得分 决定名次 ，其中名次第 1 的运动员得分最高，名次第 2 的运动员得分第 2 高，依此类推。运动员的名次决定了他们的获奖情况：

名次第 1 的运动员获金牌 "Gold Medal" 。
名次第 2 的运动员获银牌 "Silver Medal" 。
名次第 3 的运动员获铜牌 "Bronze Medal" 。
从名次第 4 到第 n 的运动员，只能获得他们的名次编号（即，名次第 x 的运动员获得编号 "x"）。
使用长度为 n 的数组 answer 返回获奖，其中 answer[i] 是第 i 位运动员的获奖情况。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-ranks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if not score: return []
        h = {s: i for i, s in enumerate(score)}
        score.sort(reverse=True)
        res = [0 for _ in range(len(score))]
        for i, s in enumerate(h):
            rank = score.index(s)
            if rank <= 2:
                res[i] = ["Gold Medal","Silver Medal","Bronze Medal"][rank]
            else:
                res[i] = str(rank+1)
        return res


        