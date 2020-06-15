from typing import *
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=2:
            return min(cost)
        pre1=cost[0];pre2=cost[1]
        tem=0
        for i in range(2,len(cost)):
            tem=min(pre1+cost[i],pre2+cost[i])
            pre1=pre2
            pre2=tem
        return min(tem,pre1)

if __name__ == '__main__':
    sol=Solution()
    cost=[10,15,20,10,10,20,10]
    print(sol.minCostClimbingStairs(cost))