from typing import *


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        for t in range(1, 27):
            num_c = 0  # 字符的个数
            c2cnt = {}  # 计数
            less = 0  # 少于k的个数
            l, r = 0, 0
            while r < n:
                if s[r] not in c2cnt:
                    c2cnt[s[r]] = 1
                    num_c += 1
                    less += 1
                else:
                    c2cnt[s[r]] += 1
                if c2cnt[s[r]] == k:
                    less -= 1

                while l <= r and num_c > t:
                    c2cnt[s[l]] -= 1
                    if c2cnt[s[l]] == k - 1:
                        less += 1
                    if c2cnt[s[l]] == 0:
                        less -= 1
                        num_c -= 1
                        del c2cnt[s[l]]
                    l += 1
                    if less == 0:
                        res = max(res, r - l + 1)
                if less == 0:
                    res = max(res, r - l + 1)
                r += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    s = 'aaabb'
    k = 2
    print(sol.longestSubstring(s, k))
