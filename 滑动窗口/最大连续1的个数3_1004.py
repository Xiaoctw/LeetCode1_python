from typing import *
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        r=0
        cnt=0
        while r<len(A) and cnt<K:
            if A[r]==0:
                cnt+=1
            r+=1
        max_len=r
        l=0
        while r<len(A):
            if A[r]==0:
                while A[l]!=0:
                    l+=1
                l+=1
            max_len=max(max_len,r-l+1)
            r+=1
        return max_len

if __name__ == '__main__':
    A = [0,0,0,1]
    K=4
    sol=Solution()
    print(sol.longestOnes(A,K))


