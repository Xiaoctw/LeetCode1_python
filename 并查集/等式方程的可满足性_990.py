class Solution:
    def equationsPossible(self, equations):
        """
        ["a==b","b==c","a==c"]
        并查集
        :type equations: List[str]
        :rtype: bool
        """
        def find(i):
            while i!=self.unionSet[i]:
                i=self.unionSet[i]
            return i

        def union(i,j):
            find_i,find_j=find(i),find(j)
            self.unionSet[find_i]=find_j

        equals,nonequals=[],[]
        self.unionSet={}
        for s in equations:
            if s[1]=='=':
                equals.append((s[0],s[3]))
            elif s[1]=='!':
                nonequals.append((s[0],s[3]))
            self.unionSet[s[0]]=s[0]
            self.unionSet[s[3]]=s[3]
        for a,b in equals:
            union(a,b)
        for a,b in nonequals:
            if find(a)==find(b):
                return False
        return True

