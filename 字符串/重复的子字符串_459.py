class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def kmp(pattern: str) -> bool:
            n = len(pattern)
            fail = [-1] * n
            for i in range(1, n):
                j = fail[i - 1]
                while j != -1 and pattern[j + 1] != pattern[i]:
                    j = fail[j]
                if pattern[j + 1] == pattern[i]:
                    fail[i] = j + 1
            return fail[n - 1] != -1 and n % (n - fail[n - 1] - 1) == 0

        return kmp(s)

if __name__ == '__main__':
    sol=Solution()
    s1='abcabcabc'
    print(sol.repeatedSubstringPattern(s1))

