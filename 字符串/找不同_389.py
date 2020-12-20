from typing import *
from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        map1 = defaultdict(lambda: 0)
        for c in t:
            map1[c] += 1
        for c in s:
            map1[c] -= 1
        for c in map1:
            if map1[c] > 0:
                return c
        return ''
