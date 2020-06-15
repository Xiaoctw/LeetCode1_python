from typing import *
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res=[0]*n
        stack=[]
        for log in logs:
            list1=log.split(':')
            id1,state,time1=list1[0],list1[1],list1[2]
            if not stack:
                stack.append((id1,int(time1)))
            else:#栈不为空
                if state=='start':
                    id2,time2=stack[-1]
                    res[int(id2)]+=(int(time1)-int(time2))
                    stack.append((id1,time1))
                else:
                    id2,time2=stack.pop()
                    res[int(id2)]+=(1+int(time1)-int(time2))
                    if stack:
                        id3,_=stack.pop()
                        stack.append((id3,int(time1)+1))
        return res

if __name__ == '__main__':
    sol=Solution()
    logs =["0:start:0",
     "1:start:2",
     "1:end:5",
     "0:end:6"]
    print(sol.exclusiveTime(2,logs))