from typing import *
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        list1=[]
        if k==0:
            return []
        list1.append(shorter*k)
        for i in range(k-1,-1,-1):
            val=i*shorter+(k-i)*longer
            if val!=list1[-1]:
                list1.append(val)
        return list1

if __name__ == '__main__':
    sol=Solution()
    shorter=1
    longer=2
    k=3
    print(sol.divingBoard(shorter,longer,k))