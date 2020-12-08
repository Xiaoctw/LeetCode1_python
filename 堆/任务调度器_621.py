from typing import *
from collections import defaultdict, Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        last_idx = {}
        que = []
        cnts = Counter(tasks)
        for c in cnts:
            heapq.heappush(que, (-cnts[c], c))
        idx = 0
        while que or last_idx:
            last = idx - n - 1
            if last in last_idx:
                heapq.heappush(que, last_idx[last])
                del last_idx[last]
            if not que:
                idx += 1
            else:
                t = heapq.heappop(que)
                if t[0] + 1 < 0:
                    last_idx[idx] = (t[0] + 1, t[1])
                idx += 1
        return idx


if __name__ == '__main__':
    sol = Solution()
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2
    print(sol.leastInterval(tasks, n))
