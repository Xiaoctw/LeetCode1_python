from collections import defaultdict
class Solution:

    def __init__(self):
        self.union_set= {}
        self.nums=defaultdict(lambda :1)

    def find(self,a):
        while a!=self.union_set[a]:
            a=self.union_set[a]
        return a

    def set_union(self,a,b):
        find_a=self.find(a)
        find_b=self.find(b)
        if find_a!=find_b:
            if  self.nums[find_a]>self.nums[find_b]:
                self.union_set[find_b]=find_a
                self.nums[find_a]+=self.nums[find_b]
                self.nums[find_b]=0
            else:
                self.union_set[find_a] = find_b
                self.nums[find_b] += self.nums[find_a]
                self.nums[find_a] = 0
        return

    def equationsPossible(self, equations):
        """
        ["a==b","b==c","a==c"]
        并查集
        :type equations: List[str]
        :rtype: bool
        """
        equals=[]; non_equals=[]
        for equ in equations:
            if '!' in equ:
                list1=equ.split('!=')
                self.union_set[list1[0]]=list1[0]
                self.union_set[list1[1]]=list1[1]
                non_equals.append((list1[0],list1[1]))
            else:
                list1=equ.split('==')
                self.union_set[list1[0]] = list1[0]
                self.union_set[list1[1]] = list1[1]
                equals.append((list1[0],list1[1]))

        for equ in equals:
            self.set_union(equ[0], equ[1])
        for a,b in non_equals:
            if self.find(a)==self.find(b):
                return False
        return True

if __name__ == '__main__':
    sol=Solution()
    equals=["a==b","b!=a"]
    print(sol.equationsPossible(equals))




