from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic1=Counter(s)
        for i,c in enumerate(s):
            if dic1[c]==1:
                return i
        return -1
