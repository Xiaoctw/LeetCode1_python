from typing import *
from collections import defaultdict


class Node:
    def __init__(self):
        self.isWord = False
        self.idx = 0
        self.nexts = defaultdict(Node)


class Solution:
    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        p = self.root
        i = len(word) - 1
        while i >= 0:
            c = word[i]
            if c in p.nexts:
                p = p.nexts[c]
                i -= 1
            else:
                break
        while i >= 0:
            node = Node()
            node.idx = i
            p.nexts[word[i]] = node
            p = node
            i -= 1
        p.isWord = True

    def judge(self, tem_s):
        i = len(tem_s) - 1
        p = self.root
        while i >= 0:
            if tem_s[i] not in p.nexts:
                return False
            p = p.nexts[tem_s[i]]
            i -= 1
        return p.isWord

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        for word in wordDict:
            self.add_word(word)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                tem_s = s[j:i]
                if self.judge(tem_s):
                    dp[i] = dp[i] or dp[j]
        if not dp[len(s)]:
            return []

        dp = {-1: ['']}
        for i in range(len(s)):
            dp[i] = []
            p = self.root
            for j in range(i, -1, -1):
                if s[j] not in p.nexts:
                    break
                p = p.nexts[s[j]]
                if p.isWord:
                    self.add_list(dp, i, s[j:i + 1], dp[j - 1])
        return dp[len(s) - 1]

    def add_list(self, dp, i, word, list1):
        for s in list1:
            if s:
                dp[i].append(s + ' ' + word)
            else:
                dp[i].append(word)


if __name__ == '__main__':
    sol = Solution()
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(sol.wordBreak(s, wordDict))
