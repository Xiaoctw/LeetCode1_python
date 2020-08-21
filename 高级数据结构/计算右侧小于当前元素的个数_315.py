from typing import *
class TreeArr():
    def __init__(self,n):
        self.n=n #原数组的长度
        self.c=[0]*(n+5)

    def lowbit(self,x): #x不可以为0
        return x & (-x)

    def update(self,i,k):
        while i<=self.n:
            self.c[i]+=k
            i+=self.lowbit(i)

    def getsum(self,i):
        res=0
        while i>0:
            res+=self.c[i]
            i-=self.lowbit(i)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        list1=list(set(nums))
        list1.sort()
        dic1={val:i+1 for i,val in enumerate(list1)}#避免数组过大，将值映射到某个范围上
        res=[]
        arr=TreeArr(len(list1))
        for i in range(len(nums)-1,-1,-1):
            idx=dic1[nums[i]]#映射到对应的值
            arr.update(idx,1)
            res.append(arr.getsum(idx-1))
        return res[::-1]

if __name__ == '__main__':
    sol=Solution()
    nums=[5,2,6,1,4,3,2,6,3,2,6,3,2,3]
    print(sol.countSmaller(nums))

