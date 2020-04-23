from typing import *
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        list1=list(num)
        # for val in list1:
        #     print(val)
        # print(list)
        stack=[]
        for c in list1:
            while k>0 and stack and ord(c)<ord(stack[-1]):
                stack.pop()
                k-=1
            stack.append(c)
        stack=stack[:len(stack)-k]
        i=0
        while i<len(stack) and stack[i]=='0':
            i+=1
        stack=stack[i:]
        if stack:
            return ''.join(stack)
        return '0'

if __name__ == '__main__':
    sol=Solution()
    print(sol.removeKdigits('1432219',3))