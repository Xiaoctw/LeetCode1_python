class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        本题利用双指针来做并不容易，
        因为两个字符串的指针指向同样的字符，选择不同的字符会影响结果。
        如果双指针加上记忆化进行回溯就可以了。
        :param s1:
        :param s2:
        :param s3:
        :return:
        '''
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                if j > 0:
                    dp[j] = dp[j] or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    s1 = "aabccreg"
    s2 = "dbbca"
    s3 = "aadbbcbcacreg"
    print(sol.isInterleave(s1, s2, s3))
