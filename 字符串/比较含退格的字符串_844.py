class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        list1 = []
        list2 = []
        for c in S:
            if c != '#':
                list1.append(c)
            elif list1:
                list1.pop()
        for c in T:
            if c != '#':
                list2.append(c)
            elif list2:
                list2.pop()
        if len(list2) != len(list1):
            return False
        for i in range(len(list1)):
            if list1[i]!=list2[i]:
                return False
        return True