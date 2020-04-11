import sys
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # Right now, dp[i] represents dp(1, i)
        dp=[[0]*(N+1) for _ in range(1+K)]
        for i in range(1,N+1):
            dp[1][i]=i
        for k in range(2,K+1):
            for n in range(1,N+1):
                dp[k][n]=sys.maxsize
                for x in range(1,n+1):
                    dp[k][n]=min(dp[k][n],1+max(dp[k-1][x-1],dp[k][n-x]))
                # while x<n and max(dp[k-1][x-1],dp[k][n-x])>=max(dp[k-1][x],dp[k][n-x-1]):
                #     x+=1
                # dp[k][n]=1+max(dp[k-1][x-1],dp[k][n-x])
        return dp[-1][-1]

if __name__ == '__main__':
    sol=Solution()
    print(sol.superEggDrop(3,14))