from typing import *


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if len(A) > len(B):
            return self.findLength(B, A)
        if len(A) == 0:
            return 0
        len1, len2 = len(A), len(B)
        lo, hi = 1, len1
        res = 0
        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            if self.judge(A, B, mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res

    def judge(self, A, B, k):
        base = 113
        val = 0
        for i in range(k):
            val = (val * base + A[i])
        set1 = set()
        set1.add(val)
        mul = int(base ** (k - 1))
        for i in range(k, len(A)):
            val = ((val % mul) * base + A[i])
            set1.add(val)
        val = 0
        for i in range(k):
            val = (val * base + B[i])
        if val in set1:
            return True
        for i in range(k, len(B)):
            val = ((val % mul) * base + B[i])
            if val in set1:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    A = [1, 0, 1, 0, 0, 0, 0, 0, 1, 1]
    B = [1, 1, 0, 1, 1, 0, 0, 0, 0, 0]
    print()
    #  print(sol.judge(A, B, 3))
    print(sol.findLength(A, B))
