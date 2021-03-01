from typing import *
from collections import defaultdict


class Solution:
    def distinctSubseqII(self, S: str) -> int:
        n = len(S)
        dp = [0] * (n + 1)
        dp[0] = 1
        mod = int(10 ** 9 + 7)
        last = defaultdict(int)
        for i, c in enumerate(S):
            dp[i + 1] = 2 * dp[i]
            if c in last:
                dp[i + 1] -= dp[last[c]]
            last[c] = i
        return (dp[len(S)] - 1) % mod


if __name__ == '__main__':
    sol = Solution()
    s = 'abc'
    print(sol.distinctSubseqII(s))
