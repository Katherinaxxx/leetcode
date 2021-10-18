'''
Author: Catherine Xiong
Date: 2021-09-08 19:16:27
LastEditTime: 2021-09-08 19:33:26
LastEditors: Catherine Xiong
Description: 给你 n 个项目。对于每个项目 i ，它都有一个纯利润 profits[i] ，和启动该项目需要的最小资本 capital[i] 。

最初，你的资本为 w 。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。

总而言之，从给定项目中选择 最多 k 个不同项目的列表，以 最大化最终资本 ，并输出最终可获得的最多资本。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ipo
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 递归 没有通过所有case
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if k == 0 or not profits:
            return w
        c = capital.pop(0)
        p = profits.pop(0)

        return max(self.findMaximizedCapital(k-1, w+p, profits, capital), self.findMaximizedCapital(k, w, profits, capital)) if w >= c else self.findMaximizedCapital(k, w, profits, capital)

# 堆排序+贪心
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        info=list(zip(profits, capital))
        info=sorted(info, key=lambda x:x[1]) # 按照所需资本数额从小到大排序
        i_proj=0 # 标记下一个应该check的项目编号
        n_proj=0 # 记录已经做过的项目数量
        prof_available=[] # 保存当前可做的项目对应的收益列表 用heapq插入/弹出
        while n_proj<k:
            # 更新(补充)可做的项目的获益列表
            while i_proj<len(info) and w>=info[i_proj][1]:
                heapq.heappush(prof_available, -info[i_proj][0])
                i_proj+=1
            # 从当前可做的项目中找到纯利润最大的
            if len(prof_available)>0:
                w+=(-heapq.heappop(prof_available))
                n_proj+=1
            else:
                break # 没有可做的项目 则跳出循环
        return w

