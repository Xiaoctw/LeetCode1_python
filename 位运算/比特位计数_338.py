from typing import *


class Solution:
    # x&(x−1),将x二进制表示中最后一个1变成0
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        highest = 0
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                highest = i
            dp[i] = dp[i - highest] + 1
        return dp


if __name__ == '__main__':
    sol = Solution()
    print(sol.countBits(20))
