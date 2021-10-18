'''
Author: Catherine Xiong
Date: 2021-08-26 22:32:54
LastEditTime: 2021-08-26 22:48:31
LastEditors: Catherine Xiong
Description: 第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/boats-to-save-people
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """先排序，再判断最小的和最大的能不能上一个船
        O(logn) O(n)
        Args:
            people (List[int]): [description]
            limit (int): [description]

        Returns:
            int: [description]
        """        
        people.sort()
        res = 0 
        i, j = 0, len(people)-1
        while i <= j:
            if i == j:
                res += 1
                break
            elif people[i] + people[j] <= limit:
                res += 1
                i += 1
                j -= 1
            elif people[j] > limit:
                return None
            else:
                res += 1 
                j -= 1
        return res
