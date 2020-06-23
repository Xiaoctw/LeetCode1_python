from typing import *
from collections import defaultdict


class Solution:
    """
    这道题利用哈希表解决。
    """

    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        ans = 0
        dic1 = defaultdict(lambda: [])
        for word in words:
            dic1[word[0]].append(word)
        for letter in S:
            old_list = dic1[letter]
            dic1[letter] = []  # 去除所有单词
            while old_list:
                s1 = old_list.pop()
                if len(s1) > 1:
                    dic1[s1[1]].append(s1[1:])
                else:
                    ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    S = 'abcde'
    words = ["abcd", "a", "bb", "acd", "ace", "ce", "c", "abe"]
    S1 = "dsahjpjauf"
    words1 = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
    print(sol.numMatchingSubseq(S, words))
    print(sol.numMatchingSubseq(S1,words1))
