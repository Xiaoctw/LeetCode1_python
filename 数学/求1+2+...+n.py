class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        '''
        巧妙利用短路方法解决问题
        短路可以代替一部分条件判断语句功能
        :param n:
        :return:
        '''
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res

if __name__ == '__main__':
    sol=Solution()
    print(sol.sumNums(30))