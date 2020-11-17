class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt, n = 0, len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        for i in range(n, 0, -1):
            for j in range(i, n + 1):
                if i == j:
                    dp[i][j] = True
                elif i == j - 1:
                    dp[i][j] = s[i - 1] == s[j - 1]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i - 1] == s[j - 1]
                if dp[i][j]:
                    cnt += 1
        return cnt




if __name__ == '__main__':
    sol = Solution()
    s1 = 'fdsklf'
    print(sol.countSubstrings(s1))
