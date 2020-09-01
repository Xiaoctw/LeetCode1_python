from typing import *


class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = [s1[::-1] for s1 in s.split()]
        return ' '.join(list1)


if __name__ == '__main__':
    sol = Solution()
    s1 = "Let's take Lee_Code contest"
    print(sol.reverseWords(s1))
