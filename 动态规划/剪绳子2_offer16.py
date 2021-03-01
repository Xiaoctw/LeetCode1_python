from typing import *
import math


class Solution:
    def cuttingRope(self, n: int) -> int:
        mod = int(10 ** 9 + 7)
        max_val = 1
        for i in range(2, n):
            val = n // i
            val2 = n % i
            max_val = max(max_val, (val + 1) ** val2 * val ** (i - val2))
        return max_val % mod


if __name__ == '__main__':
    sol = Solution()
    n = 35
    print(sol.cuttingRope(n))
