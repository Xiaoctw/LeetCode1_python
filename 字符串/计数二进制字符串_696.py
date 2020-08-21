
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i=0
        pre=0
        cnt=0
        while i<len(s):
           j=i
           while i<len(s)-1 and s[i+1]==s[i]:
              i+=1
           cnt+=min(pre,i-j+1)
           pre=(i-j+1)
           i+=1
        return cnt

if __name__ == '__main__':
    sol=Solution()
    s='10101'
    print(sol.countBinarySubstrings(s))

