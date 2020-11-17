from typing import *
from collections import defaultdict


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = defaultdict(lambda: '')
        m, n = len(str1), len(str2)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i, j] = dp[i - 1, j - 1] + str1[i - 1]
                else:
                    if len(dp[i - 1, j]) > len(dp[i, j - 1]):
                        dp[i, j] = dp[i - 1, j]
                    else:
                        dp[i, j] = dp[i, j - 1]
        s = dp[m, n]
        i, j = 0, 0
        ans = []
        for c in s:
            while i < m and str1[i] != c:
                ans.append(str1[i])
                i += 1
            while j < n and str2[j] != c:
                ans.append(str2[j])
                j += 1
            ans.append(c)
            i += 1
            j += 1
        return ''.join(ans) + str1[i:] + str2[j:]


if __name__ == '__main__':
    sol = Solution()
    str1 = "bcacaaab"
    str2 = "bbabaccc"
    s1 = "bbabacacaaabc"
    s4 = 'bcbacaaabaccc'
    print(sol.shortestCommonSupersequence(str1, str2))
