from typing import *


class Node():
    def __init__(self, c):
        self.c = c
        self.next = {}
        self.isEnd = False


class Trie():
    def __init__(self):
        self.root = Node('#')

    def add(self, word):
        node = self.root
        # 将单词倒插入字典树中
        for i in range(len(word) - 1, -1, -1):
            if word[i] not in node.next:
                node.next[word[i]] = Node(word[i])
            node = node.next[word[i]]
        node.isEnd = True


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        trie = Trie()
        for word in dictionary:
            trie.add(word)
        len1 = len(sentence)
        dp = [0] * (len1 + 1)
        for i in range(1, len1 + 1):
            dp[i] = i
            dp[i] = min(dp[i], dp[i - 1] + 1)
            node = trie.root
            for j in range(i - 1, -1, -1):
                if sentence[j] not in node.next:
                    break
                node = node.next[sentence[j]]
                if node.isEnd:
                    dp[i] = min(dp[i], dp[j])
        return dp[len1]


if __name__ == '__main__':
    sol = Solution()
    dictionary = ["looked", "just", "like", "her", "brother"]
    sentence = "jesslookedjustjustlikelovetimherbrotherthis"
    print(sol.respace(dictionary, sentence))
