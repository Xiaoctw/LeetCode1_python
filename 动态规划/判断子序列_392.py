class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        for j in range(len(t)):
            if t[j] == s[i]:
                i += 1
            if i == len(s):
                return True
        return i == len(s)


if __name__ == '__main__':
    sol = Solution()
    s = 'axc'
    t = 'ahbgdc'
    print(sol.isSubsequence(s, t))
