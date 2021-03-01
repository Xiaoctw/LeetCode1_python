from typing import *
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        leftsum=[int(boxes[0])]
        rightsum=[int(boxes[-1])]
        for i in range(1,n):
            leftsum.append(leftsum[-1]+int(boxes[i]))
        for i in range(n-2,-1,-1):
            rightsum.append(rightsum[-1]+int(boxes[i]))
        rightsum=rightsum[::-1]
        leftres=[0]*n
        for i in range(1,n):
            leftres[i]=leftres[i-1]+leftsum[i-1]
        rightres=[0]*n
        for i in range(n-2,-1,-1):
            rightres[i]=rightsum[i+1]+rightres[i+1]
        res=[]
        for i in range(n):
            res.append(leftres[i]+rightres[i])
        return res

if __name__ == '__main__':
    sol=Solution()
    boxes = "110"
    print(sol.minOperations(boxes))







