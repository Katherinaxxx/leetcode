'''
Author: Catherine Xiong
Date: 2021-12-08 18:58:38
LastEditTime: 2021-12-08 19:08:18
LastEditors: Catherine Xiong
Description: 数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 每个数字字符宽度都补成当前位数i, 那么返回第k//i个数 的 第 k%i 位即可

class Solution:
    def findNthDigit(self, k):
        i = 1
        while i * (10 ** i) < k:
            k += 10 ** i 
            i += 1
        return int(str(k//i)[k % i])

