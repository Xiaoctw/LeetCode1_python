class Solution:
    def numWays(self, s: str) -> int:
        list1 = [idx for idx in range(len(s)) if s[idx] == '1']
        mod = int(10 ** 9) + 7
        len1 = len(list1)
        if len1 % 3 != 0:
            return 0
        if len1 == 0:
            return ((len(s) - 1) * (len(s) - 2)//2) % mod
        return (list1[len1 // 3] - list1[len1 // 3 - 1]) * (list1[len1 // 3 * 2] - list1[len1 // 3 * 2 - 1]) % mod
