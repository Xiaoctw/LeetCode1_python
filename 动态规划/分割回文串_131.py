from typing import *
from collections import defaultdict


class Solution:
    def __init__(self):
        self.res = []

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        dic1 = defaultdict(lambda: [])
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif i == j - 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j]:
                    dic1[i].append(j)
        self.dfs(0, n, s, dic1, [])
        return self.res

    def dfs(self, i, n, s, dic1, tem_list):
        if i == n:
            self.res.append(tem_list[:])
            return
        for j in dic1[i]:
            tem_list.append(s[i:j + 1])
            self.dfs(j + 1, n, s, dic1, tem_list)
            tem_list.pop()


if __name__ == '__main__':
    sol = Solution()
    s = 'aabaa'
    print(sol.partition(s))
