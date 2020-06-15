from typing import *
class Solution:
    def isPalindrome(self, x: int) -> bool:
        list1=[]
        if x<0:
            return False
        while x!=0:
            list1.append(x%10)
            x//=10
        i=0;j=len(list1)-1
        while i<j:
            if list1[i]!=list1[j]:
                return False
            i+=1
            j-=1
        return True

if __name__ == '__main__':
    sol=Solution()
    num=-121
    print(sol.isPalindrome(num))