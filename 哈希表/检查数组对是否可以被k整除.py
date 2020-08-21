from typing import *
from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        '''
        遇见整除问题，首先考虑余数
        :param arr:
        :param k:
        :return:
        '''
        dic1=defaultdict(int)
        for val in arr:
            dic1[val%k]+=1
        for i in range(1,k//2+1):
            if i==k-i and dic1[i]%2!=0:
                return False
            if dic1[i]!=dic1[k-i]:
                return False
        return True

if __name__ == '__main__':
    sol=Solution()
    arr=[-1,1,-2,2,-3,3,-4,4]
    k=3
    print(-5%3)
    print(sol.canArrange(arr,k))