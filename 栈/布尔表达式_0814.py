class Solution:
    def countEval(self, s: str, result: int) -> int:
        if len(s)==0:
            return 0
        n=len(s)
        dp=[[[-1,-1] for _ in range(n)] for _ in range(n)]
        return self.rec(s,dp,0,len(s)-1,result)


    def rec(self,nums,dp,lo,hi,result):
        if lo==hi:
            return int(int(nums[lo])==result)
        if dp[lo][hi][result]!=-1:
            return dp[lo][hi][result]
        res=0
        for k in range(lo,hi,2):
            ope=nums[k+1]
            for i in {0,1}:
                for j in {0,1}:
                  if self.get_bool_res(i,j,ope)==result:
                      res+=self.rec(nums,dp,lo,k,i)*self.rec(nums,dp,k+2,hi,j)
        dp[lo][hi][result]=res
        return res



    def get_bool_res(self,i,j,operator):
        if operator=='&':
            return i and j
        if operator=='|':
            return i or j
        return i^j

if __name__ == '__main__':
    sol=Solution()
    s1='1'
    result=0
    print(sol.countEval(s1,result))