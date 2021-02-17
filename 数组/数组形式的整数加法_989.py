from typing import *


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A.reverse()
        B = []
        while K:
            B.append(K % 10)
            K //= 10
        res = []
        i, j = 0, 0
        p = 0
        while i < len(A) and j < len(B):
            res.append((A[i] + B[j] + p) % 10)
            p = (A[i] + B[j] + p) // 10
            i += 1
            j += 1
        while i < len(A):
            res.append((A[i] + p) % 10)
            p = (A[i] + p) // 10
            i += 1
        while j < len(B):
            res.append((B[j] + p) % 10)
            p = (B[j] + p) // 10
            j += 1
        if p>0:
            res.append(p)
        return res[::-1]

if __name__ == '__main__':
    sol=Solution()
    A = [1, 2, 0, 0]
    K = 1234
    print(sol.addToArrayForm(A,K))
