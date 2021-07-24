from typing import *

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder=='#':
            return True
        stack=[]
        list1=preorder.split(',')
        if list1[0]=='#':
            return False
        else:
            stack.append(2)
        for c in list1[1:]:
            if not stack:
                return False
            else:
                if c=='#':
                    if stack[-1]==0:
                        return False
                    elif stack[-1]==1:
                        stack.pop()
                    else:
                        stack[-1]-=1
                else:
                    if not stack:
                        return False
                    if stack[-1]==0:
                        return False
                    elif stack[-1]==1:
                        stack.pop()
                    else:
                        stack[-1]-=1
                    stack.append(2)
        return len(stack)==0

if __name__ == '__main__':
    sol=Solution()
    s='9'
    print(sol.isValidSerialization(s))

