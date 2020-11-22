from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1, arr2 = [0] * 26, [0] * 26
        for c in s:
            arr1[ord(c) - ord('a')] += 1
        for c in t:
            arr2[ord(c) - ord('a')] += 1
        return all([arr1[i] == arr2[i] for i in range(26)])
