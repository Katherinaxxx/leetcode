'''
Author: Catherine Xiong
Date: 2021-11-17 19:30:08
LastEditTime: 2021-11-17 19:53:14
LastEditors: Catherine Xiong
Description: 给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-word-lengths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        cset=[set(w) for w in words]
        ans=0
        for i,w in enumerate(words):
            for j in range(i+1,len(words)):
                if not cset[i]&cset[j]: # 判断两个集合是否有重叠
                    ans=max(ans,len(w)*len(words[j]))
        return ans
        
