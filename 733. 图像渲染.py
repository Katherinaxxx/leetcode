'''
Author: Catherine Xiong
Date: 2021-10-20 21:25:18
LastEditTime: 2021-10-20 21:25:18
LastEditors: Catherine Xiong
Description: 有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。

为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。

最后返回经过上色渲染后的图像。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flood-fill
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        num = image[sr][sc]
        if num == newColor: return image
        def dfs(x, y):
            if 0<=x<len(image) and 0 <= y < len(image[0]) and image[x][y] == num:
                image[x][y] = newColor
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    dfs(x+dx, y+dy)
        dfs(sr, sc)
        return image
                