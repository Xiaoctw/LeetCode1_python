from typing import *
from collections import defaultdict
import sys
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set = set(days)
     #   costs=[2,7,15]
        days=[1,7,30]
        dp=defaultdict(int)
        # for i in range(3):
        #     day=days[i]
        #     for j in range(1,366):
        #         if j in day_set:
        #             if i==0:
        #                 dp[j]=dp[j-day]+costs[i]
        #             else:
        #                 dp[j] = min(dp[j - day] + costs[i], dp[j])
        #         else:
        #             dp[j]=dp[j-1]
        for i in range(1,366):
            if i not in day_set:
                dp[i]=dp[i-1]
            else:
                dp[i]=sys.maxsize
                dp[i]=min(dp[i-days[0]]+costs[0],dp[i-days[1]]+costs[1],dp[i-days[2]]+costs[2])
        return dp[365]

if __name__ == '__main__':
    sol=Solution()
    days = [1,2,3,4,5,6,7,8,9,10,30,31]
    costs = [2, 7, 15]
    print(sol.mincostTickets(days,costs))

