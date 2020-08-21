from typing import *
from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(lambda :[])
        arr1=[0]*(numCourses)
        for req in prerequisites:
            graph[req[1]].append(req[0])
            arr1[req[0]]+=1
        que=deque([])
        for i in range(numCourses):
            if arr1[i]==0:
                que.append(i)
        num=0
        while que:
            c=que.popleft()
            num+=1
            for v in graph[c]:
                if arr1[v]>0:
                    arr1[v]-=1
                    if arr1[v]==0:
                        que.append(v)
        return num==numCourses

if __name__ == '__main__':
    sol=Solution()
    pre=[[1,0],[0,1]]
    num=2
    print(sol.canFinish(num,pre))



