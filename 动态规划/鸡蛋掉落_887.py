import sys
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # Right now, dp[i] represents dp(1, i)
        dp=[[0]*(K+1) for _ in range(N+1)]
        m=0
        while dp[m][K]<N:
            m+=1
            for j in range(1,K+1):
                dp[m][j]=dp[m-1][j-1]+dp[m-1][j]+1
        return m

if __name__ == '__main__':
    sol=Solution()
    print(sol.superEggDrop(3,14))