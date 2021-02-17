from typing import *
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) >= 2:
            val1 = heapq.heappop(stones)
            val2 = heapq.heappop(stones)
            if val1 != val2:
                heapq.heappush(stones, -abs(val2 - val1))
        if len(stones)==0:
            return 0
        return -stones[0]

if __name__ == '__main__':
    num=[2,7,4,1,8,1]
    sol=Solution()
    print(sol.lastStoneWeight(num))