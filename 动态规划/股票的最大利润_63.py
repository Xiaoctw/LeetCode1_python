from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        min_pre=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            profit=max(0,prices[i]-min_pre)
            max_profit=max(max_profit,profit)
            min_pre=min(min_pre,prices[i])
        return max_profit

if __name__ == '__main__':
    sol=Solution()
    nums=[7,1,5,3,6,4]
    print(sol.maxProfit(nums))