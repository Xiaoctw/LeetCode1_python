from typing import *
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m,n=len(A),len(B)
        dp=[[0]*(n+1) for _ in range(m+1)]
        max_val=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i-1]==B[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=0
                max_val=max(max_val,dp[i][j])
        return max_val

if __name__ == '__main__':
    sol=Solution()
    A=[1,2,3,2,1]
    B=[3,2,1,4,7]
    print(sol.findLength(A,B))