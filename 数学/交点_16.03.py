from typing import *
class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        x1,y1=start1[0],start1[1]
        x2,y2=end1[0],end1[1]
        A1=y2-y1
        B1=x1-x2
        C1=x1*y2-x2*y1
        x1, y1 = start2[0], start2[1]
        x2, y2 = end2[0], end2[1]
        A2 = y2 - y1
        B2 = x1 - x2
        C2 = x1 * y2 - x2 * y1
        if A1*B2==A2*B1:
            if A1*C2!=A2*C1:
                return []
            else:#四点一线
                if start1[0]==start2[0]:
                    if self.helper1(start1,end1,start2,end2,1):
                        return []
                    else:
                        list1 = []
                        list1.append(start1)
                        list1.append(start2)
                        list1.append(end1)
                        list1.append(end2)
                        list1.sort(key=lambda x:x[1])
                        return list1[1]
                else:
                    if self.helper1(start1,end1,start2,end2,0):
                        return []
                    list1=[]
                    list1.append(start1)
                    list1.append(start2)
                    list1.append(end1)
                    list1.append(end2)
                    list1.sort()
                    return list1[1]

        x=-(B1*C2-B2*C1)/(A1*B2-A2*B1)
        y=(A1*C2-A2*C1)/(A1*B2-A2*B1)
        return [x,y]

    def helper1(self,start1,end1,start2,end2,idx):
        if start1[idx]>start2[idx] and start1[idx]>end2[idx] and end1[idx] > start2[idx] and end1[idx] > end2[idx]:
            return True
        if start2[idx]>start1[idx] and start2[idx]>end1[idx] and end2[idx] > start1[idx] and end2[idx] > end1[idx]:
            return True
        return False


if __name__ == '__main__':
    sol=Solution()
    start1=[1,1]
    end1=[2,2]
    start2=[1,2]
    end2=[2,1]
    print(sol.intersection(start1,end1,start2,end2))

