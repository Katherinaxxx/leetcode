/*
 * @Author: Catherine Xiong 
 * @Date: 2021-08-23 23:59:20 
 * @Last Modified by: Catherine
 * @Last Modified time: 2021-08-24 00:08:47
 */

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        return (1+n)*n//2 - sum(nums)
# 二分法 O(logn) O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l , r = 0 , len(nums)-1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == mid:
                l = mid + 1
            else:
                r -= 1
        return l

