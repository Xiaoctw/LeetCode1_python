class Solution:
    def __init__(self):
        self.res = []

    def totalNQueens(self, n: int) -> int:
        self.back(0, n, [], set(), set(), set())
        return len(self.res)

    def back(self, i, n, list1, sub_set, add_set, j_set):
        if i == n - 1:
            for j in range(n):
                if i - j in sub_set or i + j in add_set or j in j_set:
                    continue
                tem_list = list1[:]
                tem_list.append(j)
                self.res.append(tem_list)
            return
        for j in range(n):
            if i - j in sub_set or i + j in add_set or j in j_set:
                continue
            sub_set.add(i - j)
            add_set.add(i + j)
            j_set.add(j)
            list1.append(j)
            self.back(i + 1, n, list1, sub_set, add_set, j_set)
            list1.pop()
            j_set.remove(j)
            add_set.remove(i + j)
            sub_set.remove(i - j)




if __name__ == '__main__':
    sol = Solution()
    print(sol.totalNQueens(8))
