class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len1,len2=len(s),len(t)
        dp=[[0]*(len2+1)for _ in range(len1+1)]
        for i in range(len1+1):
            dp[i][0]=1
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                dp[i][j]=dp[i-1][j]
                if s[i-1]==t[j-1]:
                    dp[i][j]+=dp[i-1][j-1]
        return dp[-1][-1]

if __name__ == '__main__':
    s1='rabbbit'
    s2='rabbit'
    sol=Solution()
    print(sol.numDistinct(s1,s2))
