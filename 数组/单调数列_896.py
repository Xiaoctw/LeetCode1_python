from typing import *
# class Solution {
# public:
#     bool isMonotonic(vector<int> &A) {
#         bool inc = true, dec = true;
#         int n = A.size();
#         for (int i = 0; i < n - 1; ++i) {
#             if (A[i] > A[i + 1]) {
#                 inc = false;
#             }
#             if (A[i] < A[i + 1]) {
#                 dec = false;
#             }
#         }
#         return inc || dec;
#     }
# };
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc,dec=True,True
        n=len(A)
        for i in range(n-1):
            if A[i]>A[i+1]:
                inc=False
            if A[i]<A[i+1]:
                dec=False
        return inc or dec



if __name__ == '__main__':
    sol=Solution()
    nums=[1,1,0]
    print(sol.isMonotonic(nums))