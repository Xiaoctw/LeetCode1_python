from typing import *


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for a in range(0, len(nums) - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c, d = b + 1, len(nums) - 1
                while c < d:
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d -= 1
                    else:
                        c += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [-2, -1, -1, 1, 1, 2, 2]
    print(sol.fourSum(nums, 0))
