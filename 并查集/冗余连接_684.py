class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        num = len(edges)
        self.findSet={}
        def find(i):
            while i!=self.findSet[i]:
                i=self.findSet[i]
            return i
        def union(i,j):
            find_i,find_j=find(i),find(j)
            self.findSet[find_j]=find_i
        def judge(edges,i):
            self.findSet={k:k for k in range(1,num+1)}
            for j in range(num):
                if j==i:
                    continue
                union(edges[j][0],edges[j][1])
            return len(set([find(i) for i in range(1,num+1)]))==1
        for i in range(num-1,-1,-1):
            if judge(edges,i):
                return edges[i]
        return None
    def findRedundantConnection1(self,edges):
        """
        由于这道题是树的操作,因此可以简化问题
        在寻找节点的双亲过程中,如果发现两个节点的双亲相同,那么说明这
        不是一个树,构成了环,
        那么返回false
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.findSet={}
        num=len(edges)
        def find(i):
            while i!=self.findSet[i]:
                i=self.findSet[i]
            return i
        def judge(edges,i):
            self.findSet={i:i for i in range(1,num+1)}
            for j in range(num-1,-1,-1):
                if j==i:
                    continue
                find_i=find(edges[j][0])
                find_j=find(edges[j][1])
                if find_i==find_j:
                    return False
                self.findSet[find_j]=find_i
            return True
        for i in range(num-1,-1,-1):
            if judge(edges,i):
                return edges[i]
        return None



if __name__ == '__main__':
    list1=[[1,3],[3,4],[1,5],[3,5],[2,3]]
    list2=[[1,3],[3,4],[1,5],[3,5],[2,3]]
    list3=[3,1,5,2,35,3]
    print(Solution().findRedundantConnection1(list1))
    for i in range(len(list1)-1,-1,-1):
        print(list1[i])
    for i in range(len(list3)-1,-1,-1):
        print(list3[i])
