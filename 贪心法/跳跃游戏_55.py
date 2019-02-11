class Solution:
    def canJump(self, nums):
        """
        从起始位置出发,判断能否跳到最后一个位置
        :type nums: List[int]
        :rtype: bool
        """
        l=len(nums)
        if l==0:
            return False
        i,maxDis=0,nums[0]
        while maxDis<l-1:
            pre=maxDis#保存上一次最大距离
            for j in range(i,pre+1):
                maxDis=max(maxDis,j+nums[j])
            i=pre+1#从上次判断过的下一个位置开始
            if maxDis==pre:
                return False
        return True

if __name__ == '__main__':
    l=[3,2,1,0,4]
    l1=[2,3,1,1,4]
    print(Solution().canJump(l))
    print(Solution().canJump(l1))
    print(Solution().canJump([1]))


