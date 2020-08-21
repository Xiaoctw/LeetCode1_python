
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n=len(s1),len(s2)
        if m+n!=len(s3):
            return False
        dp=[[False]*(n+1) for _ in range(m+1)]
        dp[0][0]=True 
        for i in range(m+1):
            for j in range(n+1):
                p=i+j-1
                if i>0:
                    dp[i][j]=dp[i-1][j] and s1[i-1]==s3[p]
                if j>0:
                    dp[i][j]=dp[i][j] or (dp[i][j-1] and s2[j-1]==s3[p])
        return dp[m][n]

if __name__ == '__main__':
    sol=Solution()
    s1 = "aabccreg"
    s2 = "dbbca"
    s3 = "aadbbcbcacreg"
    print(sol.isInterleave(s1,s2,s3))