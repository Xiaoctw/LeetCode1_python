from typing import *
from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        set_list1,set_list2=[set() for _ in range(n)],[set() for _ in range(n)]
        for x,y in connections:
            set_list1[x].add(y)
            set_list2[y].add(x)
        q,cnt=deque([]),0
        q.append(0)
        while q:
            root=q.popleft()
            for s in set_list1[root]:
                set_list2[s].discard(root)
                q.append(s)
            cnt+=len(set_list2[root])
            for s in set_list2[root]:
                q.append(s)
        return cnt

