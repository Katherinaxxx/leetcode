'''
Author: Catherine Xiong
Date: 2021-10-25 22:02:44
LastEditTime: 2021-10-25 22:02:44
LastEditors: Catherine Xiong
Description: 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix) - 1, len(matrix[0]) - 1
        a, b = 0, row
        while a != b:
            if target <= matrix[a][col]:
                return target in matrix[a]
            elif target >= matrix[b][0]:
                return target in matrix[b]
            else:
                a += 1
                b -= 1
        return target in matrix[a]