from typing import *
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        arr1,arr2=[1],[1]
        tem=1
        for i in range(len(a)-1):
            val=tem*a[i]
            arr1.append(val)
            tem=val
        tem=1
        for j in range(len(a)-1,0,-1):
            val=tem*a[j]
            arr2.append(val)
            tem=val
        arr2=arr2[::-1]
        res=[]
        for i in range(len(a)):
            res.append(arr1[i]*arr2[i])
        return res

if __name__ == '__main__':
    sol=Solution()
    arr=[1,2,3,4,5,6,7,8]
    print(sol.constructArr(arr))
