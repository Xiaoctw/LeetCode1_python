class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = len(s)
        dp = [[0] * (m) for _ in range(m)]
        max_res = 1
        res = ''
        for l in range(1, m + 1):
            for i in range(m - l + 1):
                j = i + l - 1
                if j - i < 2:
                    dp[i][j] = s[i] == s[j]
                    if dp[i][j]:
                        max_res = max(j - i + 1, max_res)
                        res = s[i:j + 1]
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                    if dp[i][j]:
                        max_res = max(j - i + 1, max_res)
                        res = s[i:j + 1]
        return res


if __name__ == '__main__':
    sol = Solution()
    s1 = 'cbbd'
    print(sol.longestPalindrome(s1))
