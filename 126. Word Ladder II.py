#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2019/11/1 上午11:05
@Author : Catherinexxx
@Site : 
@File : 126. Word Ladder II.py
@Software: PyCharm
"""

from collections import defaultdict


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        from collections import defaultdict
        wordList = set(wordList)
        res = []
        # 记录单词下一步能转到的单词
        next_word_dict = defaultdict(list)
        # 记录到beginWord距离
        distance = {}
        distance[beginWord] = 0

        # 找一个单词能转到的单词
        def next_word(word):
            ans = []
            for i in range(len(word)):
                for j in range(97, 123):
                    tmp = word[:i] + chr(j) + word[i + 1:]
                    if tmp != word and tmp in wordList:
                        ans.append(tmp)
            return ans

        # 求到beginWord的距离
        def bfs():
            cur = [beginWord]
            step = 0
            flag = False
            while cur:
                step += 1
                next_time = []
                for word in cur:
                    for nw in next_word(word):
                        next_word_dict[word].append(nw)
                        if nw == endWord:
                            flag = True
                        if nw not in distance:
                            distance[nw] = step
                            next_time.append(nw)
                if flag:
                    break
                cur = next_time
            # 遍历所有从beginWord到endWord的路径

        def dfs(tmp, step):
            if tmp[-1] == endWord:
                res.append(tmp)
                return
            for word in next_word_dict[tmp[-1]]:
                if distance[word] == step + 1:
                    dfs(tmp + [word], step + 1)

        bfs()
        dfs([beginWord], 0)
        return res


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list) -> list:
        wordList = set(wordList)  # 转换为hash实现O(1)的in判断
        if endWord not in wordList:
            return []
        # 分别为答案、用于剪枝的已访问哈希，前向分支和后向分支，当前的前向分支以及后向分支中的路径和的长度
        # 前向路径分支与后向路径分支的字典结构为{结束词：到达该结束词的路径列表}
        res, visited, forward, backward, _len = [], set(), {beginWord: [[beginWord]]}, {endWord: [[endWord]]}, 2
        while forward:
            if len(forward) > len(backward):  # 始终从路径分支较少的一端做BFS
                forward, backward = backward, forward
            tmp = {}  # 存储新的前向分支
            while forward:
                word, paths = forward.popitem()  # 取出路径结束词以及到达它的所有路径
                visited.add(word)  # 记录已访问
                for i in range(len(word)):
                    for a in 'abcdefghijklmnopqrstuvwxyz':
                        new = word[:i]+a+word[i+1:]  # 对结束词尝试每一位的置换
                        if new in backward:  # 如果在后向分支列表里发现置换后的词，则路径会和
                            if paths[0][0] == beginWord:  # 前向分支是从beginWord开始的，添加路径会和的笛卡尔积
                                res.extend(fPath + bPath[::-1] for fPath in paths for bPath in backward[new])
                            else:  # 后向分支是从endWord开始的，添加路径会和的笛卡尔积
                                res.extend(bPath + fPath[::-1] for fPath in paths for bPath in backward[new])
                        if new in wordList and new not in visited:  # 仅当wordList存在该词且该词还未碰见过才进行BFS
                            tmp[new] = tmp.get(new, []) + [path + [new] for path in paths]
            _len += 1
            if res and _len > len(res[0]):  # res已有答案，且下一次BFS的会和路径长度已超过当前长度，不是最短
                break
            forward = tmp  # 更新前向分支
        return res

print(Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))