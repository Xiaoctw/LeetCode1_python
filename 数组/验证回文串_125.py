from typing import *
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=[c.lower() for c in s if c.isalnum()]
        i,j=0,len(s1)-1
        while i<=j:
            if s1[i]!=s1[j]:
                return False
            i+=1
            j-=1
        return True

if __name__ == '__main__':
    sol=Solution()
    s1='A man, a plan, a canal: Panama'
    print(sol.isPalindrome(s1))