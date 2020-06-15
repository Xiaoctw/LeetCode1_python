from typing import *
from collections import defaultdict
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cnt=defaultdict(int)
        self.words=set()

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.words.add(word)
            for i in range(len(word)):
                word1=word[:i]+'*'+word[i+1:]
                self.cnt[word1]+=1



    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for i in range(len(word)):
            word1=word[:i]+'*'+word[i+1:]
            if self.cnt[word1]>1 or (self.cnt[word1]==1 and word not in self.words):
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)