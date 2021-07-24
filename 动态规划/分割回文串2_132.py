from typing import *
import sys


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp1 = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp1[i][j] = True
                elif i == j - 1:
                    dp1[i][j] = s[i] == s[j]
                else:
                    dp1[i][j] = dp1[i + 1][j - 1] and s[i] == s[j]

        dp2=[n]*n
        for i in range(n):
            if dp1[0][i]:
                dp2[i]=0
            else:
                for j in range(i):
                    if dp1[j+1][i]:
                        dp2[i]=min(dp2[i],dp2[j]+1)
        return dp2[-1]


if __name__ == '__main__':
    sol = Solution()
    s = 'aba'
    print(sol.minCut(s))
