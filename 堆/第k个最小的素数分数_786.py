from typing import *
import heapq


class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        que = []
        for i in range(len(A) - 1):
            for j in range(len(A) - 1, i, -1):
                heapq.heappush(que,(A[i]/A[j],A[i],A[j]))
        for _ in range(K-1):
            heapq.heappop(que)
        return [que[0][1],que[0][2]]



if __name__ == '__main__':
    sol = Solution()
    A = [1, 2,3,5]
    K = 3
    print(sol.kthSmallestPrimeFraction(A, K))
