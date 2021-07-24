from typing import *


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = []
        n1 = n
        while n:
            nums.append(n % 10)
            n //= 10
        nums.reverse()
        self.nextPermutation(nums)
        res = 0
        for val in nums:
            res = res * 10 + val
        if res == n1 or res > (2 ** 31 - 1):
            return -1
        return res

    # 首先如果是降序排列的话那么就不会有更大的排列了，
    # 从右向左找时，需要找到nums[i-1]<nums[i]，
    # 此时在从i位置到末尾中找到刚好比nums[i-1]要大的那个元素，假设位置为j，
    # 然后交换nums[i-1]和nums[j]，在将i到末尾元素交换
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i - 1 >= 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            return None
        idx = i - 1
        j = i
        while j + 1 < len(nums) and nums[j + 1] > nums[idx]:
            j += 1
        nums[idx], nums[j] = nums[j], nums[idx]
        i = idx + 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    n = 54123
    sol = Solution()
    print(sol.nextGreaterElement(n))
