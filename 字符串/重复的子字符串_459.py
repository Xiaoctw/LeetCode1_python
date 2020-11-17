class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        pnext = self.getNext(s)
        print(pnext)
        len1 = len(s)
        return pnext[len1 - 1] != 0 and len1 % (len1 - pnext[len1 - 1]) == 0

    def getNext(self,substr):
        idx, m = 0, len(substr)
        onexit = [0] * m
        i = 1
        while i < m:
            if substr[i] == substr[idx]:
                onexit[i] = idx + 1
                idx += 1
                i += 1
            else:
                if idx != 0:
                    idx = onexit[idx - 1]
                else:
                    onexit[i] = 0
                    i += 1
        return onexit




if __name__ == '__main__':
    sol = Solution()
    s1 = 'abac'
    print(sol.repeatedSubstringPattern(s1))
