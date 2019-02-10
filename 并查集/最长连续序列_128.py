class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums=sorted(nums)
        max_val,i=1,0
        while i<len(nums)-1:
            j=i+1
            while j<len(nums) and (nums[j]==nums[j-1]+1 or nums[j]==nums[j-1]):
                j+=1
            max_val=max(max_val,nums[j-1]-nums[i]+1)
            i=j
        return max_val

if __name__ == '__main__':
    nums=[100,4,200,1,3,2]
    nums1=[0,-1]
    print(Solution().longestConsecutive(nums))
    print(Solution().longestConsecutive(nums1))

