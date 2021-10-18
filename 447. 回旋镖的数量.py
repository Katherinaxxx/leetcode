'''
Author: Catherine Xiong
Date: 2021-09-13 20:01:16
LastEditTime: 2021-09-13 20:22:19
LastEditors: Catherine Xiong
Description: 给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

返回平面上所有回旋镖的数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-boomerangs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# hash
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for x1, y1 in points:
            # cnts 是与(x1,y1)距离k的点的数量
            cnts = defaultdict(int)
            for x2, y2 in points:
                # 计算距离
                dx, dy = x1 - x2, y1 - y2
                d = dx ** 2 + dy ** 2
                # 考虑顺序
                ans += cnts[d]
                cnts[d] += 1
        return ans * 2

