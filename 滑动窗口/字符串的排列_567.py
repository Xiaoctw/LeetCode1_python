class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1>n2:
            return False
        a1 = [0] * 26
        for c in s1:
            a1[ord(c) - ord('a')] += 1
        for i in range(n1):
            a1[ord(s2[i]) - ord('a')] -= 1
        if self.judge(a1):
            return True
        for i in range(n1, n2):
            a1[ord(s2[i]) - ord('a')] -= 1
            a1[ord(s2[i - n1]) - ord('a')] += 1
            if self.judge(a1):
                return True
        return False

    def judge(self, a):
        for val in a:
            if val != 0:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    s1 = "ab"
    s2 = "eidboaoo"
    print(sol.checkInclusion(s1, s2))
