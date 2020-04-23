from typing import *
class Solution:
    def __init__(self):
        self.res=[]
    def generateParenthesis(self, n: int) -> List[str]:
        self.generate('',0,0,n)
        return self.res
    def generate(self,s,i1,j1,n):
        if i1<j1 or i1>n or j1>n:
            return
        if i1==n and j1==n-1:
            s1=s+')'
            self.res.append(s1)
            return
        s1=s+'('
        s2=s+')'
        self.generate(s1,i1+1,j1,n)
        self.generate(s2,i1,j1+1,n)

if __name__ == '__main__':
    sol=Solution()
    print(sol.generateParenthesis(3))