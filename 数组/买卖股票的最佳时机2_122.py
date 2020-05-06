from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(1,len(prices)):
            #只要第二天比第一天多，就加上
            if prices[i]>prices[i-1]:
                res+=(prices[i]-prices[i-1])
        return res

if __name__ == '__main__':
    sol=Solution()
    nums=[7,1,5,3,6,4]
    print(sol.maxProfit(nums))
