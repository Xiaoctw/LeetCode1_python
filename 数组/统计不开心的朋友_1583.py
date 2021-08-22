from typing import *
from collections import defaultdict
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pre_set=defaultdict(lambda :set())
        idx2pair={}
        res_set=set()
        for pair in pairs:
            idx2pair[pair[0]]=pair[1]
            idx2pair[pair[1]]=pair[0]
        for i,preference in enumerate(preferences):
            for j in preference:
                if j==idx2pair[i]:
                    break
                pre_set[i].add(j)
        for i in range(n):
            if i in res_set:
                continue
            for j in pre_set[i]:
                if i in pre_set[j]:
                    res_set.add(i)
                    res_set.add(j)
        return len(res_set)

if __name__ == '__main__':
    n = 2
    preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
    pairs =[[1, 3], [0, 2]]
    sol=Solution()
    print(sol.unhappyFriends(n,preferences,pairs))
