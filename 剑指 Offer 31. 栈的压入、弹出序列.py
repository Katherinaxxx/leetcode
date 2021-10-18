'''
Author: Catherine Xiong
Date: 2021-09-05 20:59:27
LastEditTime: 2021-09-05 21:13:43
LastEditors: Catherine Xiong
Description: 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 判断合不合法，用个栈试一试: 把压栈的元素按顺序压入，当栈顶元素和出栈的第一个元素相同，则将该元素弹出，出栈列表指针后移并继续判断。最后判断出栈列表指针是否指向出栈列表的末尾即可
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        s = []
        for x in pushed:
            s.append(x)
            while s and s[-1] == popped[j]:
                s.pop(-1)
                j += 1
        return j == len(popped) 