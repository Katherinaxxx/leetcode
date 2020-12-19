# # 1、BFS O(nc^2)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        set_list = set(wordList)
        if not wordList or endWord not in set_list:
            return 0
        visited = {beginWord, endWord}
        left, right = {beginWord}, {endWord}
        number = 0
        length = len(beginWord)
        # 当前层中数量少的给left,多的给right
        while left:
            number += 1
            next_level = set()
            for word in left:
                for j in range(length):
                    for m in range(26):
                        new_word = word[:j] + chr(ord('a') + m) + word[j + 1:]
                        if new_word in right:
                            return number + 1
                        if new_word not in visited and new_word in set_list:
                            visited.add(new_word)
                            next_level.add(new_word)
            left = next_level
            if len(left) > len(right):
                left, right = right, left
        return 0



class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList: return 0

        front = {beginWord}
        # back = {endWord}
        dist = 1  # 走的步数
        wordList = set(wordList)
        word_len = len(beginWord)
        while front:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(word_len):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        # for c in string.lowercase:

                        if c != word[i]:
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word == endWord:
                                return dist
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)
            front = next_front
            # if len(back)<len(front):
            #     front, back = back, front
        return 0


# 双端BFS
# import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList: return 0

        front = {beginWord}
        back = {endWord}
        dist = 1  # 走的步数
        wordList = set(wordList)    # set查删的更快
        word_len = len(beginWord)
        while front and back:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(word_len):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        # for c in string.lowercase:

                        if c != word[i]:
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in back:
                                return dist
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)   # 防止重复走
            front = next_front
            # 双端
            if len(back) < len(front):
                front, back = back, front
        return 0