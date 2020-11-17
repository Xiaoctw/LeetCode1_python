class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        list1 = self.helper(name)
        list2 = self.helper(typed)
        if len(list1) != len(list2):
            return False
        for i in range(len(list1)):
            if list1[i][0] != list2[i][0] or list1[i][1] > list2[i][1]:
                return False
        return True

    def helper(self, s):
        c, cnt = '$', 1
        list1 = []
        for i in range(len(s)):
            if s[i] == c:
                cnt += 1
            else:
                list1.append((c, cnt))
                cnt = 1
                c = s[i]
        list1.append((c, cnt))
        return list1[1:]


if __name__ == '__main__':
    sol = Solution()
    name = 'leretttt'
    typed = 'leereettt'
    print(sol.helper(typed))
