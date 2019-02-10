class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def find(i):
            """
            找到某一个人的根
            :param i:
            :return:
            """
            while i!=self.findSet[i]:
                i=self.findSet[i]
            return i
        def union(i,j):
            """
            进行合并操作
            :param i:
            :param j:
            :return:
            """
            find_i,find_j=find(i),find(j)
            self.findSet[find_j]=find_i
        num_person=len(M)
        self.findSet={i:i for i in range(num_person)}#findSet为直接上级,find函数返回根
        for i in range(num_person):
            for j in range(num_person):
                if M[i][j]:
                    union(i,j)
        return len([i for i in range(num_person) if find(i)==i])
