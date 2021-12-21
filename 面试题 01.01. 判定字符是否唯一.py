'''
Author: Catherine Xiong
Date: 2021-12-16 20:25:52
LastEditTime: 2021-12-16 20:40:57
LastEditors: Catherine Xiong
Description: 
'''
class Solution:
    def isUnique(self, astr: str) -> bool:
        if len(astr) <= 1:
            return True
        astr = [s for s in astr]
        astr.sort()
        for i in range(1, len(astr)):
            if astr[i] == astr[i-1]: return False
        return True
