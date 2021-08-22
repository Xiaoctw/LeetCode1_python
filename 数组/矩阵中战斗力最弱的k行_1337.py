from typing import *
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        cnts=[sum(mat[i]) for i in range(len(mat))]
        idxes=list(range(len(cnts)))
        idxes.sort(key=lambda x:cnts[x])
        return idxes[:k]

if __name__ == '__main__':
    sol=Solution()
    mat=[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
    print(sol.kWeakestRows(mat,3))