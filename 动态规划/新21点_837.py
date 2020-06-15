from typing import *
class Solution:
    #dp[i]为从i点开始抓，最终得到的结果是多少
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp=[0]*(K+W+1)
        s=0
        for i in range(K,min(N+1,K+W)):
            dp[i]=1
            s+=1
        for i in range(K-1,-1,-1):
            dp[i]=s/W
            s=s-dp[i+W]+dp[i]
        return dp[0]

if __name__ == '__main__':
    sol=Solution()
    print(sol.new21Game(21,17,10))
