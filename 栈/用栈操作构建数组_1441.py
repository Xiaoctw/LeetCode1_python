from typing import *
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        idx=0
        tem=0
        res=[]
        while idx<len(target):
            tem+=1
            res.append('Push')
            while tem!=target[idx]:
                res.append('Pop')
                tem+=1
                res.append('Push')
            idx+=1
        return res

if __name__ == '__main__':
    sol=Solution()
    target=[2,3,4]
    n=4
    print(sol.buildArray(target,n))
