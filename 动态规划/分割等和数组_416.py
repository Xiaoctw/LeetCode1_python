from typing import *


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        m = len(nums)
        dp = [0] * (total_sum + 1)
        for i in range(1, m + 1):
            for j in range(target, nums[i - 1] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i - 1]] + nums[i - 1])
        if dp[target] == target:
            return True
        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 5]
    print(sol.canPartition(nums))
