from typing import *
from collections import defaultdict
import sys


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set = set(days)
        days = [1, 7, 30]
        dp = defaultdict(int)  # 为了避免数组越界采用这样的方法进行处理
        for i in range(1, 366):
            if i not in day_set:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[i - days[0]] + costs[0], dp[i - days[1]] + costs[1], dp[i - days[2]] + costs[2])
        return dp[365]


if __name__ == '__main__':
    sol = Solution()
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs = [2, 7, 15]
    print(sol.mincostTickets(days, costs))
