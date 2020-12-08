from typing import *


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] = self.helper(A[i][j])
        for j in range(n):
            cnt1 = 0
            for i in range(m):
                if A[i][j] > 0:
                    cnt1 += 1
            if cnt1 <= m // 2:
                for i in range(m):
                    A[i][j] = self.helper(A[i][j])
        res=0
        for i in range(m):
            tem=A[i][0]
            for j in range(1,n):
                tem=tem*2+A[i][j]
            res+=tem
        return res


    def helper(self, val):
        if val == 0:
            return 1
        return 0

if __name__ == '__main__':
    sol=Solution()
    nums=[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    print(sol.matrixScore(nums))
