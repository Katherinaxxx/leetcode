'''
Author: Catherine Xiong
Date: 2021-08-31 22:50:53
LastEditTime: 2021-08-31 22:52:12
LastEditors: Catherine Xiong
Description: 这里有 n 个航班，它们分别从 1 到 n 进行编号。

有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/corporate-flight-bookings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 遍历 O(n^2) time 超时 
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0 for _ in range(n)]
        for booking in bookings:
            for i in range(booking[0]-1, booking[1]):
                res[i] += booking[2]
        return res
# 差分数组+前缀和 O(n)time
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        # 注意与下标相差1
        for first, last, seat in bookings:
            res[first-1] += seat
            # 防止下标越界
            if last < n:
                res[last] -= seat
        return list(accumulate(res))

