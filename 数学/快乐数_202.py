from typing import *
class Solution:
    '''
    寻找快乐数
    '''
    def isHappy(self, n: int) -> bool:
        set1=set()
        while True:
            if n in set1:
                return False
            set1.add(n)
            n=self.helper1(n)
            if n==1:
                return True

    def helper1(self,val):
        res=0
        while val!=0:
            res+=(val%10)**2
            val//=10
        return res

if __name__ == '__main__':
    sol=Solution()
    n=233333
    print(sol.isHappy(n))