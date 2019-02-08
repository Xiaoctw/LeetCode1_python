class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        x=y=di=0
        obstacleSet=set(map(tuple,obstacles))
        ans=0
        # for cmd in commands:
        #     if cmd==-1:
        #
