from typing import *
class Solution:
    def maximumTime(self, time: str) -> str:
        res=[]
        if time[0]=='?':
            if time[1]=='?' or int(time[1])<=3:
                 res.append('2')
            else:
                res.append('1')
        else:
            res.append(time[0])
        if time[1]=='?':
            if res[-1]=='2':
                res.append('3')
            else:
                res.append('9')
        else:
            res.append(time[1])
        res.append(':')
        if time[3]=='?':
            res.append('5')
        else:
            res.append(time[3])
        if time[4]=='?':
            res.append('9')
        else:
            res.append(time[4])
        return ''.join(res)


if __name__ == '__main__':
    sol=Solution()
    time = "1?:22"
    print(sol.maximumTime(time))