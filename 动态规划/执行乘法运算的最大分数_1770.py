from typing import *
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        dp = [[0 for _ in range(1005)] for _ in range(1005)]

        res = -0x3f3f3f3f

        for k in range(1, m + 1):  # 取的总个数
            for i in range(0, k + 1):  # 左边取的个数
                j = k - i  # 右边取的个数
                if i == 0:  # 都是从右边取的
                    dp[i][j] = dp[i][j - 1] + nums[-k] * multipliers[k - 1]
                elif i == k:  # 都是从左边取的
                    dp[i][j] = dp[i - 1][j] + nums[k - 1] * multipliers[k - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j] + nums[i - 1] * multipliers[k - 1],
                                   dp[i][j - 1] + nums[-j] * multipliers[k - 1])
                if k == m:
                    res = max(res, dp[i][j])
        return res







if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    multipliers = [3,2,1]
    print(sol.maximumScore(nums, multipliers))
