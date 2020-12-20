from typing import *


class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = []
        while num:
            num_list.append(num % 10)
            num //= 10
        num_list.reverse()
        max_tuple = tuple(num_list)
        for i in range(len(num_list)):
            for j in range(i + 1, len(num_list)):
                num_list[i], num_list[j] = num_list[j], num_list[i]
                tem_tuple = tuple(num_list)
                if tem_tuple > max_tuple:
                    max_tuple = tem_tuple
                num_list[i], num_list[j] = num_list[j], num_list[i]
        ans = 0
        for val in max_tuple:
            ans = ans * 10 + val
        return ans


if __name__ == '__main__':
    N = 9973
    sol = Solution()
    print(sol.maximumSwap(N))
