from typing import *
import sys


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A:
            return 0
        dp1 = [1] * len(A)
        dp2 = [1] * len(A)
        dp1[0] = 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                dp1[i] = dp1[i - 1] + 1
        dp2[len(A) - 1] = 1
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                dp2[i] = dp2[i + 1] + 1
        max_val = 0
        for i in range(len(A)):
            if dp1[i] > 1 and dp2[i] > 1:
                max_val = max(max_val, dp1[i] + dp2[i] - 1)
        return max_val


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 2, 2]
    print(sol.longestMountain(nums))
