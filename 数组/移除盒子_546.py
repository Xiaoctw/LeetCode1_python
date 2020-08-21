from typing import *
from collections import defaultdict
class Solution:
    def __init__(self):
        self.dic=defaultdict(int)
    def removeBoxes(self, boxes: List[int]) -> int:
        return self.helper(boxes,0,len(boxes)-1,0)

    def helper(self,boxes,l,r,k):
        if l>r:
            return 0
        if self.dic[l,r,k]!=0:
            return self.dic[l,r,k]
        while r>l and boxes[r]==boxes[r-1]:
            r-=1
            k+=1
        self.dic[l,r,k]=self.helper(boxes,l,r-1,0)+(k+1)*(k+1)
        for i in range(l,r):
            if boxes[i]==boxes[r]:
                self.dic[l,r,k]=max(self.dic[l,r,k],self.helper(boxes,l,i,k+1)+self.helper(boxes,i+1,r-1,0))
        return self.dic[l,r,k]

if __name__ == '__main__':
    sol=Solution()
    nums=[1, 3, 2, 2, 2, 3, 4, 3, 1]
    print(sol.removeBoxes(nums))