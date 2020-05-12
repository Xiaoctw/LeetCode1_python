from typing import *
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        x1=x
        x2=(1/2)*(x1+x/x1)
        while x1-x2>1e-6:
            x1=x2
            x2=(1/2)*(x1+x/x1)
        return int(x2)


if __name__ == '__main__':
    sol=Solution()
    print(sol.mySqrt(100000000))

