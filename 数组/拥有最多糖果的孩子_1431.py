from typing import *
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val=max(candies)
        res=[val+extraCandies>=max_val for val in candies]
        return res

if __name__ == '__main__':
    sol=Solution()
    print(sol.kidsWithCandies([2,3,5,1,3],3))
