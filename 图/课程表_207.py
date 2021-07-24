from typing import *
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees=[0]*numCourses
        graph=defaultdict(lambda :[])
        for pre in prerequisites:
            indegrees[pre[0]]+=1
            graph[pre[1]].append(pre[0])

        que=deque([])
        for i in range(numCourses):
            if indegrees[i]==0:
                que.append(i)

        num=0

        while que:
            len1=len(que)
            for _ in range(len1):
                j=que.popleft()
                num+=1
                for k in graph[j]:
                    indegrees[k]-=1
                    if indegrees[k]==0:
                        que.append(k)

        return num==numCourses







if __name__ == '__main__':
    sol = Solution()
    pre = [[1, 0], [0, 1]]
    num = 2
    print(sol.canFinish(num, pre))
