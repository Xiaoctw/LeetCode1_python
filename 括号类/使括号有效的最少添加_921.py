from typing import *
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack=[]
        cnt=0
        for c in S:
            if c=='(':
                stack.append(c)
            else:
                if not stack:
                    cnt+=1
                else:
                    stack.pop()
        return cnt+len(stack)

if __name__ == '__main__':
    sol=Solution()
    s='()))(('
    print(sol.minAddToMakeValid(s))