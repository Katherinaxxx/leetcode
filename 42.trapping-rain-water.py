'''
Author: Catherine Xiong
Date: 2019-10-24 11:39:01
LastEditTime: 2021-11-04 22:07:14
LastEditors: Catherine Xiong
Description: 
'''
# class Solution:
#     def trap(self, h):
#         res = 0
#         i = 0
#         s = []
#         j = 0
#         while j < len(h) and i < len(h):
#             j = i + 1
#             if j == len(h) or h[i] <= h[j]:
#                 i += 1
#                 continue
#             while j < len(h) and h[i] > h[j]:
#                 s.append(h[j])
#                 j += 1
#                 if j == len(h)-1 and h[i] > h[j]:
#                     i += 1
#                     j = i + 1
#                     s = []
#                     continue
#             water = sum(h[i] - s[_] for _ in range(len(s)))
#             res = res + water
#             i = j
#             s = []
#         return res

# class Solution:
#     def trap(self, h):
#         res = 0
#         i = 0
#         while i <= len(h)-1:
#             l, r = i - 1, i + 1
#             tmp = i
#             # 找左边最大边界l+1
#             while l >= 0 and h[l] >= h[tmp]:
#                 tmp = l
#                 l -= 1
#             tmp = i
#             # 找右边最大边界r-1
#             while r <= len(h)-1 and h[r] >= h[tmp]:
#                 tmp = r
#                 r += 1
#             # 若不存在左右大值
#             if h[l+1] <= h[i] or h[r-1] <= h[i]:
#                 i += 1
#                 pass
#             else:
#                 # res += min(h[l+1], h[r-1])*(r-l-3)-sum(h[l+2:r-1])
#                 res += sum([(min(h[l+1], h[r-1]) - x) for x in h[l+2:r-1] if x < min(h[l+1], h[r-1])])
#                 i = r - 1
#         return res

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        stack = []
        res = 0
        for i in range(n):

            while stack and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                if not stack: break
                res += (min(height[i], height[stack[-1]]) - height[tmp]) * (i-stack[-1] - 1)
            stack.append(i)
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h1 = 0
        h2 = 0
        for i in range(len(height)):
            h1 = max(h1,height[i])
            h2 = max(h2,height[-i-1])
            ans = ans + h1 + h2 -height[i]
        return  ans - len(height)*h1