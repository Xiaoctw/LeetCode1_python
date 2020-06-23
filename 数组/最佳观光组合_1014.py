from typing import *
import sys


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        dic1 = {}
        stack = []
        for i, val in enumerate(A):
            while stack and A[stack[-1]] < val:
                j = stack.pop()
                dic1[j] = i
            stack.append(i)
        for val in stack:
            dic1[val] = -1
        max_val = -sys.maxsize
        for i in range(len(A) - 1):
            j = i + 1
            max_val = max(max_val, A[i] + A[j] - abs(i - j))
            while dic1[j] != -1:
                j = dic1[j]
                max_val = max(max_val, A[i] + A[j] - abs(i - j))
        return max_val


if __name__ == '__main__':
    sol = Solution()
    nums = [8, 1, 5, 2, 6]
    print(sol.maxScoreSightseeingPair(nums))
