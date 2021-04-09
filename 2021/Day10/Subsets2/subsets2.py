class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        dic = {}
        if len(nums) == 0:
            return [[]]

        def permute(combo, index):
            dic[tuple(sorted(combo))] = dic.get(tuple(sorted(combo)), 0)+1
            if dic[tuple(sorted(combo))] > 1:
                return
            out.append(combo)
            if len(combo) == len(nums):
                return
            for i in range(index, len(nums)):
                permute(combo+[nums[i]], i+1)
            return out
        return permute([], 0)
