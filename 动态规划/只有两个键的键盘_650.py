from typing import *
class Solution:
    '''
    分解质因数
    '''
    def minSteps(self, n: int) -> int:
        ans=0
        d=2
        while n>1:
            while n%d==0:
                ans+=d
                n/=d
            d+=1
        return ans

if __name__ == '__main__':
    sol=Solution()
    print(sol.minSteps(30))
