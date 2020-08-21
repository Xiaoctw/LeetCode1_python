from typing import *
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        tem=0,0
        dic={'N':(0,1),'S':(0,-1),'E':(-1,0),'W':(1,0)}
        set1=set()
        set1.add(tem)
        for c in path:
            tem=tem[0]+dic[c][0],tem[1]+dic[c][1]
            if tem in set1:
                return True
            set1.add(tem)
        return False

if __name__ == '__main__':
    sol=Solution()
    print(sol.isPathCrossing('NESWW'))