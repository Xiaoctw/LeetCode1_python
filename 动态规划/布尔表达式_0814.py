from collections import defaultdict
class Solution:
    def __init__(self):
        self.dp=defaultdict(int)
    def countEval(self, s: str, result: int) -> int:
        return self.helper1(s,0,len(s)-1,result)

    def helper1(self,s,i,j,result):
        if (i,j,result) in self.dp:
            return self.dp[i,j,result]
        if i==j:
            if int(s[i])==result:
                return 1
            return 0
        for k in range(i,j,2):
            ope=s[k+1]
            for val1 in {0,1}:
                for val2 in {0,1}:
                    if self.get_res(val1,val2,ope)==result:
                        self.dp[i,j,result]+=self.helper1(s,i,k,val1)*self.helper1(s,k+2,j,val2)
        return self.dp[i,j,result]


    def get_res(self,val1,val2,ope):
        if ope=='&':
            return val1 and val2
        elif ope=='|':
            return val1 or val2
        return val1 ^ val2


if __name__ == '__main__':
    sol=Solution()
    s1='0&0&0&1^1|0'
    result=1
    print(sol.countEval(s1,result))