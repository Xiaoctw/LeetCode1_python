from typing import *


class Solution:
    # 转化为01背包问题
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        m = len(stones)
        dp = [[0] * (total_sum + 1) for _ in range(m + 1)]
        target = total_sum // 2
        for i in range(1, m + 1):
            for j in range(total_sum):
                if j<stones[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - stones[i-1]] + stones[i-1],dp[i-1][j])
        return total_sum - 2 * dp[m][target]


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2]
    print(sol.lastStoneWeightII(nums))
