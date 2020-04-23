class Solution:
    def waysToChange(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        for coin in {1,5,10,25}:
            #为了避免重复，一次首先使用一种找零方式
            for i in range(coin,n+1):
                dp[i]=(dp[i]+dp[i-coin])%1000000007
        return dp[n]

if __name__ == '__main__':
    sol=Solution()
    print(sol.waysToChange(10000))