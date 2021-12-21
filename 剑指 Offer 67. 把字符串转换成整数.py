'''
Author: Catherine Xiong
Date: 2021-12-06 18:47:46
LastEditTime: 2021-12-06 19:10:33
LastEditors: Catherine Xiong
Description: 写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。

 

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def strToInt(self, str: str) -> int:
        res, i, sign = 0, 0, 1
        max_int, min_int, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        # delete ' '
        while i < len(str) and str[i] == ' ':
            i += 1
        if i == len(str): return 0
        if str[i] == '-': sign = -1
        if str[i] in '-+': i += 1
        for s in str[i:]:
            if not '0' <= s <= '9': break
            if res > bndry or res == bndry and s > '7': # 已超界 or 下一步超界
                return min_int if sign == -1 else max_int
            res = res * 10 + ord(s) - ord('0')
        return sign * res