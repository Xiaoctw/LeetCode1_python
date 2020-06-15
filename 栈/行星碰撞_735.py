from typing import *
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for val in asteroids:
            if val<0:
                if not stack or stack[-1]<0:
                    stack.append(val)
                else:
                    flag = False
                    while stack and stack[-1]>0 and stack[-1]<abs(val):
                        stack.pop()
                    if stack and stack[-1]==abs(val):
                        flag=True
                        stack.pop()
                    if stack and stack[-1]>abs(val):
                        flag=True
                    if not flag:
                        stack.append(val)
            else:
                stack.append(val)
        return stack

if __name__ == '__main__':
    sol=Solution()
    ast=[-2,-2,1,-2]
    print(sol.asteroidCollision(ast))
