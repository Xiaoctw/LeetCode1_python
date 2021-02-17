from typing import *
from collections import defaultdict


class Solution:
    def __init__(self):
        self.max_time = 0
        self.map1 = defaultdict(lambda: [])

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        for i, m in enumerate(manager):
            if m == -1:
                continue
            else:
                self.map1[m].append(i)
        self.dfs(headID, 0, informTime)
        return self.max_time

    def dfs(self, i, time, informTime):
        time += informTime[i]
        self.max_time = max(self.max_time, time)
        for j in self.map1[i]:
            self.dfs(j, time, informTime)

if __name__ == '__main__':
    n = 7
    headID = 6
    manager = [1, 2, 3, 4, 5, 6, -1]
    informTime = [0, 6, 5, 4, 3, 2, 1]
    sol=Solution()
    print(sol.numOfMinutes(n,headID,manager,informTime))
