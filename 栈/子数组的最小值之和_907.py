from typing import *
class Solution:
    '''
    利用递增栈实现
    '''
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack=[]
        res=0
        tmp=0#这个tmp代表栈中的和
        mod=10**9+7
        for i in range(len(A)):
            cnt=1
            while stack and A[i]<=stack[-1][0]:
                cur=stack.pop()
                cnt+=cur[1]#代表在这个元素之前有多少个大于等于它的数字
                tmp-=cur[0]*cur[1]
            stack.append((A[i],cnt))
            tmp+=A[i]*cnt
            res+=tmp
            res%=mod
        return res



if __name__ == '__main__':
    sol=Solution()
    nums=[3,1,2,4]
    print(sol.sumSubarrayMins(nums))
