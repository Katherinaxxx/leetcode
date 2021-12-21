'''
Author: Catherine Xiong
Date: 2021-12-09 18:42:08
LastEditTime: 2021-12-09 18:59:10
LastEditors: Catherine Xiong
Description: 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
"""
计算左右两个方向的累乘数组
然后在遍历一次即可
time O(n) space O(n)
也可以看做dp
"""
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        b, tmp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1] # 下三角 left
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]            # 上三角 right
            b[i] *= tmp                # 下三角 * 上三角
        return b

        