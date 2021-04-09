class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(list(range(len(nums)+1))) - sum(nums)
