from typing import *
class Solution:


    def check(self,matrix,val):
        m,n=len(matrix),len(matrix[0])
        i,j=m-1,0
        cnt=0
        while i>=0 and j<n:
            if matrix[i][j]<=val:
                cnt+=(i+1)
                j+=1
            else:
                i-=1
        return cnt


    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l,r=matrix[0][0],matrix[-1][-1]
        res=l
        while l<=r:
            mid=(l+r)//2
            num=self.check(matrix,mid)
            if num>=k:#找到的为最小的l，最小的l正好在数组中
                #大于等于时要向左搜索
                r=mid-1
            else:
                l=mid+1
        return l


if __name__ == '__main__':
    sol=Solution()
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k=9
    print(sol.kthSmallest(matrix,k))
