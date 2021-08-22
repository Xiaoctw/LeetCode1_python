from typing import *
from collections import defaultdict,deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        g=defaultdict(lambda :set())
        g1=defaultdict(lambda :set())
        for i,nums in enumerate(graph):
            for num in nums:
                g[i].add(num)
                g1[num].add(i)
        que=deque([])
        for i in range(n):
            if len(g[i])==0:
                que.append(i)
        res=[]
        while que:
            que_len=len(que)
            for _ in range(que_len):
                node=que.popleft()
                res.append(node)
                for node1 in g1[node]:
                    g[node1].remove(node)
                    if len(g[node1])==0:
                        que.append(node1)
        res.sort()
        return res

if __name__ == '__main__':
    graph =[[1,2,3,4],[1,2],[3,4],[0,4],[]]
    sol=Solution()
    print(sol.eventualSafeNodes(graph))


