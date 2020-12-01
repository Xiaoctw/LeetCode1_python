from typing import *
import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        que = [1]
        set1 = set()
        set1.add(1)
        while n:
            val = heapq.heappop(que)
            n -= 1
            if n == 0:
                return val
            for prime in primes:
                if val * prime not in set1:
                    heapq.heappush(que, val * prime)
                    set1.add(val*prime)


if __name__ == '__main__':
    sol = Solution()
    primes = [2, 7, 13, 19]
    n = 1
    print(sol.nthSuperUglyNumber(n, primes))
