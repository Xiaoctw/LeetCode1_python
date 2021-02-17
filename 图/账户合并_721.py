from typing import *
from collections import defaultdict


class Solution:
    def __init__(self):
        self.arr = None

    def find(self, i):
        if i != self.arr[i]:
            self.arr[i] = self.find(self.arr[i])
        return self.arr[i]

    def set_union(self, i, j):
        find_i = self.find(i)
        find_j = self.find(j)
        if find_i != find_j:
            self.arr[find_i] = find_j

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        self.arr = [i for i in range(len(accounts))]
        self.account2idx = defaultdict(lambda: -1)
        set1 = set()
        for i in range(len(accounts)):
            for account in accounts[i][1:]:
                set1.add(account)
                if self.account2idx[account] != -1:
                    self.set_union(i, self.account2idx[account])
                else:
                    self.account2idx[account] = i
        dic1 = defaultdict(lambda: [])
        for account in set1:
            dic1[self.find(self.account2idx[account])].append(account)
        list1 = []
        for i in dic1:
            new_list = [accounts[i][0]]
            new_list.extend(sorted(dic1[i]))
            list1.append(new_list)
        return list1

if __name__ == '__main__':
    sol=Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    print(sol.accountsMerge(accounts))
