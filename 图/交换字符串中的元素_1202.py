from typing import *
from collections import defaultdict


class Solution:
    def __init__(self):
        self.arr = None

    def find(self, i):
        if i != self.arr[i]:
            self.arr[i] = self.find(self.arr[i])
        return self.arr[i]

    def set_union(self, i, j):
        find_i = self.find(i)
        find_j = self.find(j)
        if find_j != find_i:
            self.arr[find_j] = find_i

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        len1 = len(s)
        self.arr = [i for i in range(len1)]
        for pair in pairs:
            self.set_union(pair[0], pair[1])
        dic1 = defaultdict(lambda: [])
        for i in range(len1):
            dic1[self.find(i)].append(s[i])
        for i in dic1:
            dic1[i] = sorted(dic1[i])
        dic2 = defaultdict(int)
        res = []
        for i in range(len1):
            set_idx = self.find(i)
            res.append(dic1[set_idx][dic2[set_idx]])
            dic2[set_idx] += 1
        return ''.join(res)


if __name__ == '__main__':
    s = "dcab"
    pairs = [[0,3],[1,2],[0,2]]
    sol = Solution()
    print(sol.smallestStringWithSwaps(s, pairs))
