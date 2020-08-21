from typing import *
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g=self.gcd(p,q)
        p=(p/g)%2
        q=(q/g)%2
        if p and q:
            return 1
        if p==1:
            return 0
        return 2



    def gcd(self,a,b):
        if a==0:
            return b
        return self.gcd(b%a,a)