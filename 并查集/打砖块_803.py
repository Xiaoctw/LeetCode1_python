class Solution:
    def hitBricks(self, grid, hits):
        """
        打砖块,找到掉下去的砖块数目
        注意砖块是依次消除的,之前的操作会对后面产生影响
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        def find(i):
            """
            :param i:
            :return: 如果连着
            """
            while self.unionSet[i] not in {-1,-2}:
                i=self.unionSet[i]
            return self.unionSet[i]
        mov_x,mov_y=[-1,0,1,0],[0,1,0,-1]
        m,n=len(grid),len(grid[0])
        for hit in hits:#删除掉所有要打掉的点
            grid[hit[0]][hit[1]]=0
        self.unionSet={i:-1 for i in range(n)}#第一排都不会掉下去





