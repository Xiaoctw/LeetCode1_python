from collections import defaultdict
class Solution:
    def __init__(self):
        self.dp= defaultdict(lambda :-1)

    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(0,0,s,p)==1

    def helper(self,i,j,s,p):
        if self.dp[i,j]!=-1:
            return self.dp[i,j]
        if j==len(p):
            self.dp[i,j]=i==len(s)
            return self.dp[i,j]
        if j+1<len(p) and p[j+1]=='*':
            res=self.helper(i,j+2,s,p)
            for k in range(i,len(s)):
                if p[j] in {s[k],'.'}:
                    res=res or self.helper(k+1,j+2,s,p)
                else:
                    break
            self.dp[i,j]=res
            return self.dp[i,j]
        if i<len(s) and p[j] in {s[i],'.'}:
            self.dp[i,j]=self.helper(i+1,j+1,s,p)
            return self.dp[i,j]
        self.dp[i,j]=False
        return self.dp[i,j]

if __name__ == '__main__':
    sol=Solution()
    s='mississippi'
    p='mis*is*p*.'
    print(sol.isMatch(s,p))