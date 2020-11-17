from typing import *


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i = 0
        while i < len(A):
            if A[i] % 2 != i % 2:
                j = i + 1
                while j < len(A) and not (A[j] % 2 != j % 2 and j % 2 != i % 2):
                    j += 1
                A[i], A[j] = A[j], A[i]
            i += 1
        return A

if __name__ == '__main__':
    sol=Solution()
    nums=[4, 2, 5, 7]
    print(sol.sortArrayByParityII(nums))
