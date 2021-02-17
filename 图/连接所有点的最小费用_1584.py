from typing import *
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        from queue import PriorityQueue
        cal = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])  

        pq = PriorityQueue()
        visited = set([i for i in range(len(points))])
        res = 0

        pq.put((0, 0))  
        while visited: 
            dis, now = pq.get()  
            if now not in visited: 
                continue
            visited.remove(now)
            res += dis
            for i in visited:
                pq.put((cal(points[now], points[i]), i))  

        return res