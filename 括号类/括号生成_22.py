from typing import *
class Solution:
    '''
    递归实现
    '''
    def __init__(self):
        self.res=[]
    def generateParenthesis(self, n: int) -> List[str]:
        self.generate('',0,0,0,n)
        return self.res

    def generate(self,s,i,num_left,num_right,n):
        if num_right>num_left:
            return
        if i==2*n-1 and num_left==n and num_right==n-1:
            s1=s+')'
            self.res.append(s1)
            return
        if i==2*n-1:
            return
        s1=s+'('
        self.generate(s1,i+1,num_left+1,num_right,n)
        s2=s+')'
        self.generate(s2,i+1,num_left,num_right+1,n)