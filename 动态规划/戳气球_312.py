from typing import *


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        ext_nums = [1] * (n + 2)
        for i in range(n):
            ext_nums[i + 1] = nums[i]
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(n, 0, -1):
            for j in range(i, n + 1):
                if i == j:
                    dp[i][j] = ext_nums[i] * ext_nums[i - 1] * ext_nums[i + 1]
                else:
                    dp[i][j] = ext_nums[i - 1] * ext_nums[i] * ext_nums[j + 1] + dp[i + 1][j]
                    dp[i][j] = max(dp[i][j], ext_nums[j + 1] * ext_nums[j] * ext_nums[i - 1] + dp[i][j - 1])
                    for k in range(i + 1, j):
                        dp[i][j] = max(dp[i][j],
                                       dp[i][k - 1] + dp[k + 1][j] + ext_nums[k] * ext_nums[i - 1] * ext_nums[j + 1])
        return dp[1][n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxCoins([3, 1, 5, 8]))
