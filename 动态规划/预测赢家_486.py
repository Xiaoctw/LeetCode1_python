from typing import *


class Solution:

    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        # 对角线的动态规划问题的改进方法，从倒数第二行开始向前推进
        # 这也是为什么从后开始
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 5, 233, 7]
    print(sol.PredictTheWinner(nums))
