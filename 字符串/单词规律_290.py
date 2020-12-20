from typing import *


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p2s = {}
        s2p = {}
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        for i, c in enumerate(pattern):
            s = s_list[i]
            if c not in p2s and s not in s2p:
                p2s[c] = s
                s2p[s]=c
            elif c not in p2s and s in s2p:
                return False
            elif c in p2s and s not in s2p:
                return False
            else:
                if s != p2s[c]:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    pattern = "abba"
    str = "dog dog dog dog"
    print(sol.wordPattern(pattern, str))
