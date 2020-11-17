from typing import *
from collections import deque, defaultdict


class Solution:
    def __init__(self):
        self.graph = defaultdict(lambda: set())

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        for prerequisite in prerequisites:
            self.graph[prerequisite[1]].add(prerequisite[0])
        res = []
        set1 = set()
        que = deque([])
        for i in range(numCourses):
            if not self.graph[i]:
                que.append(i)
        while que:
            tem = que.popleft()
            res.append(tem)
            set1.add(tem)
            for key in self.graph:
                if tem in self.graph[key]:
                    self.graph[key].remove(tem)
                    if not self.graph[key] and key not in set1:
                        que.append(key)
        # 说明存在环，无法全部加入课程表
        if len(res) != numCourses:
            return []
        return res[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findOrder(3, [[0, 2], [1, 2], [2, 0]]))
