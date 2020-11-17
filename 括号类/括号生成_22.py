from typing import *


class Solution:
    """
    利用卡特兰数的构造方法进行构造
    """
    def __init__(self):
        self.dic1 = {0: [''],
                     1: ['()']}

    def generateParenthesis(self, n: int) -> List[str]:
        return self.helper(n)

    def helper(self, n):
        if n in self.dic1:
            return self.dic1[n]
        list1 = []
        for i in range(n):
            for left in self.helper(i):
                for right in self.helper(n - 1 - i):
                    list1.append('({}){}'.format(left, right))
        self.dic1[n] = list1
        return list1


if __name__ == '__main__':
    sol = Solution()
    n = 3
    print(sol.generateParenthesis(n))
