from typing import *
class Solution:
    def __init__(self):
        self.dp={}
    def numTrees(self, n: int) -> int:
        return self.helper(n)

    def helper(self,val):
        if val in self.dp:
            return self.dp[val]
        if val==1 or val==0:
            return 1
        res=0
        for i in range(1,val+1):
            l=self.helper(i-1)
            r=self.helper(val-i)
            res+=l*r
        self.dp[val]=res
        return res

if __name__ == '__main__':
    sol=Solution()
    print(sol.helper(40))