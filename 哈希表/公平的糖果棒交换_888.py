from typing import *
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A,sum_B=sum(A),sum(B)
        set1=set(A)
        for val in B:
            val1=(sum_A-sum_B)//2+val
            if val1 in set1:
                return [val1,val]
        return None

if __name__ == '__main__':
    sol=Solution()
    A = [1, 1]
    B = [2, 2]
    print(sol.fairCandySwap(A,B))
