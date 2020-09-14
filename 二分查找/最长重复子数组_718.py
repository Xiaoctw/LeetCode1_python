from typing import *


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        res = 0
        lo, hi = 0, min(len(A), len(B))
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.check(A, B, mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res

    def check(self, A, B, len1):
        mod = 10 ** 9 + 9
        base = 113
        mult = int(base ** (len1 - 1))
        val_set = set()
        val1 = 0
        for j in range(len1):
            val1 = (val1 * base + A[j]) % mod
        val_set.add(val1)
        for i in range(1, len(A) - len1 + 1):
            val1 = ((val1 - A[i - 1] * mult % mod) * base + A[i + len1 - 1]) % mod
            val_set.add(val1)
        val1 = 0
        for j in range(len1):
            val1 = (val1 * base + B[j]) % mod
        if val1 in val_set:
            return True
        for i in range(1, len(B) - len1 + 1):
            val1 = ((val1 - B[i - 1] * mult % mod) * base + B[i + len1 - 1]) % mod
            if val1 in val_set:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    A = [1, 2, 3, 2, 4, 5, 6, 1, 1, 1, 1, 1, 1, 1]
    B = [3, 2, 1, 1, 4, 7, 4, 5, 6, 1, 1, 1, 1, 1, 1]
    print(sol.findLength(A, B))
