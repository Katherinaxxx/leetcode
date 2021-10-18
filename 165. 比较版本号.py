'''
Author: Catherine Xiong
Date: 2021-09-01 23:40:27
LastEditTime: 2021-09-01 23:50:57
LastEditors: Catherine Xiong
Description: 给你两个版本号 version1 和 version2 ，请你比较它们。

版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。例如，2.5.33 和 0.1 都是有效的版本号。

比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。也就是说，修订号 1 和修订号 001 相等 。如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。例如，版本 1.0 小于版本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 0 和 1 ，0 < 1 。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compare-version-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# O(max(m,n))
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = 0
        p2 = 0

        while p1 < len(version1) or p2 < len(version2):
            num1 = 0
            num2 = 0
            while p1 < len(version1) and version1[p1] != '.':
                num1 = num1 * 10 + int(version1[p1])
                p1 += 1
            
            while p2 < len(version2) and version2[p2] != '.':
                num2 = num2 * 10 + int(version2[p2])
                p2 += 1
            
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            # 跳过 .
            p1 += 1
            p2 += 1
        return 0
