from typing import *


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if changed:
                    return False
                changed = True
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return True

if __name__ == '__main__':
    sol=Solution()
    nums=[4,2,1]
    print(sol.checkPossibility(nums))
