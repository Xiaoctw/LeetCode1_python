from typing import *


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        list1 = [('&', nums[0])]
        for i in range(1, len(nums)):
            if list1[-1][0] == '&':
                if nums[i] > list1[-1][1]:
                    list1.append(('u', nums[i]))
                elif nums[i] < list1[-1][1]:
                    list1.append(('d', nums[i]))
            elif list1[-1][0] == 'u':
                if nums[i] > list1[-1][1]:
                    list1.pop()
                    list1.append(('u', nums[i]))
                elif nums[i] < list1[-1][1]:
                    list1.append(('d', nums[i]))
            else:
                if nums[i] < list1[-1][1]:
                    list1.pop()
                    list1.append(('d', nums[i]))
                elif nums[i] > list1[-1][1]:
                    list1.append(('u', nums[i]))
        return len(list1)


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sol.wiggleMaxLength(nums))
