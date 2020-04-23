from typing import *
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i]=dp[i]+dp[i-coin]
        return dp[-1]

if __name__ == '__main__':
    sol=Solution()
    amount=10
    coins=[10]
    print(sol.change(amount,coins))