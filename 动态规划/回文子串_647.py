from typing import *
class Solution:
    def countSubstrings(self, s: str) -> int:
        m = len(s)
        dp = [[0] * (m) for _ in range(m)]
        cnt=0
        for l in range(1, m + 1):
            for i in range(m - l + 1):
                j = i + l - 1
                if j - i < 2:
                    dp[i][j] = s[i] == s[j]
                    if dp[i][j]:
                        cnt+=1
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                    if dp[i][j]:
                        cnt+=1
        return cnt
