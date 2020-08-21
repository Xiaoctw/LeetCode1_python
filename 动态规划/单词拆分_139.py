from typing import *
class TrieTree:
    def __init__(self):
        self.head=Node('#')

    def add(self,word):
        tem=self.head
        for c in word:
            if c not in tem.next:
                tem.next[c]=Node(c)
            tem=tem.next[c]
        tem.isLeaf=True

    def contains(self,word):
        tem=self.head
        for c in word:
            if c not in tem.next:
                return False
            tem=tem.next[c]
        return tem.isLeaf


class Node:
    def __init__(self,c):
        self.c=c
        self.isLeaf=False
        self.next={}


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # trie=TrieTree()
        trie=set()
        trie.add('')
        [trie.add(word) for word in wordDict]
        len1=len(s)
        dp=[False]*(len1+1)
        dp[0]=True
        for i in range(len1+1):
            for j in range(i):
                dp[i]=dp[i] or (dp[j] and s[j:i] in trie)
        return dp[len1]


if __name__ == '__main__':
    sol=Solution()
    s='leetcodethis'
    wordDict=['1','leet','code','this']
    print(sol.wordBreak(s,wordDict))
    