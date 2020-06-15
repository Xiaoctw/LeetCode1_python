from typing import *
class Solution:
    '''
    这里利用矩阵乘法实现
    '''
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        mat1=self.pow_matrix(n-1)
        return mat1[1][0]*2+mat1[1][1]
    def pow_matrix(self,n):
        if n==1:
            return [[1,1],[1,0]]
        mat1=self.pow_matrix(n//2)
        if n % 2 == 0:
            return self.product_mat(mat1,mat1)
        mat2=[[1,1],[1,0]]
        mat1=self.product_mat(mat1,mat1)
        return self.product_mat(mat1,mat2)
    def product_mat(self,mat1,mat2):
        a = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
        b = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
        c = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
        d = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]
        return [[a, b], [c, d]]



if __name__ == '__main__':
    sol=Solution()
    print(sol.climbStairs(7))