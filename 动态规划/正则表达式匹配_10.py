from collections import defaultdict


class Solution:
    def __init__(self):
        self.dp={}

    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(s,p,0,0)


    def helper(self,s,p,i,j):
        if (i, j) in self.dp:
            return self.dp[i, j]

        if i==len(s):
            if len(p)==j:
                self.dp[i,j]=True
                return True
            # if j==len(p)-2 and p[j+1]=='*':
            #     self.dp[i, j] = True
            #     return True

            #结尾有多个 a*b*之类的
            if j+1<len(p) and p[j+1]=='*':
                if self.helper(s,p,i,j+2):
                    return True
            return False
        if j==len(p):
            self.dp[i, j] = False
            return False

        # if j==len(p):
        #     self.dp[i,j]=len(s)==i
        #     return self.dp[i,j]

        if i==len(s):
            return False

        if j<len(p)-1 and p[j+1]=='*':
            if self.helper(s,p,i,j+2):
                self.dp[i, j] = True
                return True
            for k in range(i,len(s)):
                if p[j] not in {s[k],'.'}:
                    break
                if self.helper(s,p,k+1,j+2):
                    self.dp[i, j] = True
                    return True
            return False
        if p[j] in {s[i],'.'}:
            if self.helper(s,p,i+1,j+1):
                self.dp[i,j]=True
                return True
        self.dp[i, j] = False
        return False


if __name__ == '__main__':
    sol=Solution()
    s="abcaaaaaaabaabcabac"
    p=".*ab.a.*a*a*.*b*b*"
    print(sol.isMatch(s,p))








