from collections import defaultdict
class Solution:
    def __init__(self):
        self.dp= {}
    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(s,p,0,0)

    def helper(self,s,p,i,j):
        if (i,j) in self.dp:
            return self.dp[i,j]
        if j==len(p):
            self.dp[i,j]=i==len(s)
            return self.dp[i,j]
        if p[j]=='*':
            if i>len(s):
                self.dp[i,j]=False
            else:
                self.dp[i,j]=self.helper(s,p,i,j+1) or self.helper(s,p,i+1,j)
            return self.dp[i,j]
        if i<len(s) and p[j] in {s[i],'?'}:
            self.dp[i,j]=self.helper(s,p,i+1,j+1)
            return self.dp[i,j]
        self.dp[i,j]=False
        return False

if __name__ == '__main__':
    sol=Solution()
    s1='acdcb'
    p='a*c?b'
    print(sol.isMatch(s1,p))