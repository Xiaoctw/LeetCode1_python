class Solution:
    def combinationSum(self, candidates, target):
        sorted_list = sorted(candidates)
        res = []

        def find_list(list, tar, index):
            # if index>=len(sorted_list):
            #     return
            if tar < sorted_list[index]:
                return
            if tar == sorted_list[index]:
                lis = list[:]
                lis.append(sorted_list[index])
                res.append(lis)
                return
            # list.append(sorted_list[index])
            for i in range(index, len(sorted_list)):
                lis = list[:]
                lis.append(sorted_list[index])
                find_list(lis, tar - sorted_list[index], i)

        # find_list([],target,0)
        for i in range(len(sorted_list)):
            find_list([], target, i)
        return res


if __name__ == '__main__':
    obj = Solution()
    res = obj.combinationSum([2, 3, 6, 7], target=7)
    print(res)
