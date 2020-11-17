from typing import *
class Solution:
    def __init__(self):
        self.res=[]

    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        list1=[]
        for i in range(4):
            val=int(s[:i+1])
            if str(val)!=s[:i+1]:
                continue
            if 0<=val<=255:
                list1.append(s[:i+1])
                self.search(s,i,list1,1)
                list1.pop()
        return self.res


    def search(self,s,idx,list1,cnt):
        if idx==len(s)-1 and cnt==4:
            self.res.append(''.join(list1))
            return
        if cnt==4 or idx>=len(s):
            return
        list1.append('.')
        for i in range(idx+1,idx+4):
            if i>=len(s):
                break
            val=int(s[idx+1:i+1])
            if s[idx+1:i+1]!=str(val):
                continue
            if 0<=val<=255:
                list1.append(s[idx+1:i+1])
                self.search(s,i,list1,cnt+1)
                list1.pop()
        list1.pop()

if __name__ == '__main__':
    sol=Solution()
    s='010010'
    print(sol.restoreIpAddresses(s))