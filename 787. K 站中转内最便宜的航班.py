'''
Author: Catherine Xiong
Date: 2021-08-24 22:36:11
LastEditTime: 2021-08-24 22:46:12
LastEditors: Catherine Xiong
Description: 有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。

现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cheapest-flights-within-k-stops
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = [[float("inf")] * n for _ in range(k + 2)]
        f[0][src] = 0
        for t in range(1, k + 2):
            for j, i, cost in flights:
                f[t][i] = min(f[t][i], f[t - 1][j] + cost)
        
        ans = min(f[t][dst] for t in range(1, k + 2))
        return -1 if ans == float("inf") else ans


# dijkstra
import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if len(flights) == 0:
            return -1

        neibghbours = collections.defaultdict(list)
        for i, j, p in flights:
            neibghbours[i].append([j, p])
        
        # 检查起点和终点间是否有通路，没有则返回 -1
        visited = set()
        q = [src]
        while q:
            position = q.pop()
            visited.add(position)
            for nei, _ in neibghbours[position]:
                if nei not in visited:
                    q.append(nei)
        
        if dst not in visited:
            return -1

        # 用优先队列选择符合条件的最低价格
        pq = [[0, -1, src]]
        while pq:
            price, passed, position = heapq.heappop(pq)
            if position == dst:
                return price
            for nei_position, nei_price in neibghbours[position]:
                if passed + 1 <= k:
                    heapq.heappush(pq, [price+nei_price, passed+1, nei_position])

        return -1
