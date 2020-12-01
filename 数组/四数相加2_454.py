from typing import *
from collections import defaultdict


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic1 = defaultdict(int)
        for a in A:
            for b in B:
                dic1[a + b] += 1
        res = 0
        for c in C:
            for d in D:
                res += dic1[-(c + d)]
        return res


if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    sol = Solution()
    print(sol.fourSumCount(A, B, C, D))
